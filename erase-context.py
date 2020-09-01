from blip_session import BlipSession

my_auth_key = '{{bot_auth_key}}'
bs = BlipSession(my_auth_key)
user_id = '{{phone_number}}@wa.gw.msging.net'
ccrb = {
    'method' : 'get',
    'uri' : f'/contexts/{user_id}'
} 

response = bs.force_command(ccrb)
print(response)
context_variables = response['resource']['items']


for context in context_variables:
    
    bs.process_command({
        'method': 'delete',
        'uri': f'/contexts/{user_id}/{context}'
    })


