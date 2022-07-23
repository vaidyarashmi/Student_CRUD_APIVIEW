import requests
import json
BASE_URL='http://127.0.0.1:8000/'
END_URL='api/'

'''
def get_resource(id=None):
    data={}
    if id is not None:
        data={
            'id':id
        }
    resp=requests.get(BASE_URL+END_URL,data=json.dumps(data))
    print(resp.json())
    print(resp.status_code)
get_resource()
'''
"""
def create_resource():
    new_stud={
        'roll_no': 80,
        'name': 'rasika', 
        'address': 'ooty', 
        'mobile_number': 8978675645, 
        'marks': 89.0
    }
    resp=requests.post(BASE_URL+END_URL,data=json.dumps(new_stud))
    print(resp.json())
    print(resp.status_code)
create_resource()
"""
"""
def update_resource(id=None):
    new_stud={
        'address': 'banglore', 
        'marks':99.0,
        'id':id
    }
    resp=requests.put(BASE_URL+END_URL,data=json.dumps(new_stud))
    print(resp.json())
    print(resp.status_code)

update_resource()
"""
"""
def delete_resource(id=None):
    data={
        'id':id
    }
    resp=requests.delete(BASE_URL+END_URL,data=json.dumps(data))
    print(resp.json())
    print(resp.status_code)

delete_resource()
"""


