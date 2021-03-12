import sys
import json
from blip_session import BlipSession

PUBLISH_FLAG = '-publish' 
CONFIG_VAR_FLAG = '-config'
def get_flow(blip_session, type_key = 'blip_portal:builder_published_flow'):
    get_flow_rb = {
            'method' : 'get',
            'uri' : f'/buckets/{type_key}'
        }

    new_flow = blip_session.force_command(get_flow_rb)
    return new_flow

def publish_flow(blip_session, new_flow, type_key = 'blip_portal:builder_published_flow'):
    try:
        set_flow(blip_session, new_flow)
        publish_flow_rb = {
            'method' : 'set',
            'uri' : f'/buckets/{type_key}',
            'type': 'application/json',
            'resource': new_flow['resource']
        }
        publish_response = blip_session.force_command(publish_flow_rb)
        return publish_response['status']
    except:
        print(new_flow['description'])

def set_flow(blip_session, new_flow, type_key = 'blip_portal:builder_working_flow'):
    try:
        set_flow_rb = {
            'method' : 'set',
            'uri' : f'/buckets/{type_key}',
            'type': 'application/json',
            'resource': new_flow['resource']
        }
        print(blip_session)
        response = blip_session.force_command(set_flow_rb)
        print(response)
        return response['status']
    except:
        print(new_flow['description'])
    

if len(sys.argv) < 4:
    print('use: python deploy_flow.py <file>')
    print('Obs: If you want to directly publish add the flag -publish after file')
    exit(-1)

bots_file = open(sys.argv[1], 'r', encoding='utf8')
bot_list = json.load(bots_file)
origin_flow = sys.argv[2]
destiny_flow = sys.argv[3]
is_publish = False
is_config = False
if len(sys.argv) == 5 and sys.argv[4] == PUBLISH_FLAG:
    is_publish = True
elif len(sys.argv) == 5 and sys.argv[4] == CONFIG_VAR_FLAG:
    is_config = True
    type_key = 'blip_portal:builder_published_configuration'
bots_file.close()


for bot in bot_list:
    origin_session = BlipSession(bot[origin_flow])
    destiny_session = BlipSession(bot[destiny_flow])
    print(destiny_session)
    new_flow = get_flow(origin_session, type_key)
    type_key = ''
        
    if is_publish:
        current_flow = publish_flow(destiny_session, new_flow)
        print(current_flow)
    elif is_config:
        current_flow = set_flow(destiny_flow, new_flow, type_key)
    else:
        current_flow = set_flow(destiny_session, new_flow)

    if current_flow == 'success':
        print(f"Fluxo {bot['Id']}-{origin_flow} carregado em {bot['Id']}-{destiny_flow}")
    else:
        print(f"Falha ao carregar {bot['Id']}-{origin_flow} em {bot['Id']}-{destiny_flow}")
