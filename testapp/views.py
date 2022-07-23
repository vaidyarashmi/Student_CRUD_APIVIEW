from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Student
from testapp.forms import StudentForm
from django.views.generic import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.mixins import Http_Response_mixins,serailizer_mixins

# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(Http_Response_mixins,serailizer_mixins,View):
    def get_data_by_id(self,id):
        try:
            stud=Student.objects.get(id=id)
        except:
            stud=None
        return stud
    
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json only'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)      
        if id is not None:
            stud=self.get_data_by_id(id)
            if stud is None:
                json_data=json.dumps({'msg':'The no matched resource found, Not possible to perform opeartion'})
                return self.render_to_http_response(json_data,status=400)
            json_data=self.serialize([stud,])
            return self.render_to_http_response(json_data,status=200)
        stud=Student.objects.all()
        json_data=self.serialize(stud)
        return self.render_to_http_response(json_data,status=200)

    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json only'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'Please enter id for delete operation'})
            return self.render_to_http_response(json_data,status=400)
        stud=self.get_data_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'The no matched resource found, Not possible to perform deletion'})
            return self.render_to_http_response(json_data,status=400)
        status,deleted_items=stud.delete()
        if status==1:
            json_data=json.dumps({'msg':'deleted successfully'})
            return self.render_to_http_response(json_data,status=200)
        json_data=json.dumps({'msg':'unable to perform deletion, Please try after some time'})
        return self.render_to_http_response(json_data,status=400)
    
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json only'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        form=StudentForm(p_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'created successfully'})
            return self.render_to_http_response(json_data,status=200)    
        if form.errors:        
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
        
    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json only'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is None:
            json_data=json.dumps({'msg':'Please enter id for update operation'})
            return self.render_to_http_response(json_data,status=400)
        stud=self.get_data_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'The no matched resource found, Not possible to perform updation'})
            return self.render_to_http_response(json_data,status=400)
        original_data={
            'roll_no': stud.roll_no,
            'name': stud.name, 
            'address': stud.address, 
            'mobile_number': stud.mobile_number, 
            'marks': stud.marks
        }
        provided_data=json.loads(data)
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=stud)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'updated successfully'})
            return self.render_to_http_response(json_data,status=200)    
        if form.errors:        
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
         
