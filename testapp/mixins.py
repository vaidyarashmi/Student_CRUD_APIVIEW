from django.http import HttpResponse
import json
from django.core.serializers import serialize
class Http_Response_mixins(object):
    def render_to_http_response(self,json_data,status):
        return HttpResponse(json_data,content_type='application/json',status=status)

class serailizer_mixins(object):
    def serialize(self,stud):
        final_list=[]
        json_data=serialize('json',stud)
        p_data=json.loads(json_data)
        for object in p_data:
            stud_data=object['fields']
            final_list.append(stud_data)
        json_data=json.dumps(final_list)
        return json_data