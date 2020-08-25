import sys
import json
from blip_session import BlipSession


def get_flow(blip_session):
    get_flow_rb = {
            'method' : 'get',
            'uri' : '/buckets/blip_portal:builder_published_flow'
        }

    new_flow = blip_session.force_command(get_flow_rb)
    return new_flow

def set_flow(blip_session, new_flow):
    try:
        set_flow_rb = {
            'method' : 'set',
            'uri' : f'/buckets/blip_portal:builder_working_flow',
            'type': 'application/json',
            'resource': new_flow['resource']
        }
        response = blip_session.force_command(set_flow_rb)
        return response['status']
    except:
        print(new_flow['description'])
    

if len(sys.argv) < 4:
    print('uso: python deploy_flow.py <arquivo>')
    exit(-1)

bots_file = open(sys.argv[1], 'r', encoding='utf8')
bot_list = json.load(bots_file)
origin_flow = sys.argv[2]
destiny_flow = sys.argv[3]
bots_file.close()


for bot in bot_list:
    origin_session = BlipSession(bot[origin_flow])
    destiny_session = BlipSession(bot[destiny_flow])
    new_flow = get_flow(origin_session)
    current_flow = set_flow(destiny_session, new_flow)
    if current_flow == 'success':
        print(f"Fluxo {bot['Id']}-{origin_flow} carregado em {bot['Id']}-{destiny_flow}")
    else:
        print(f"Falha ao carregar {bot['Id']}-{origin_flow} em {bot['Id']}-{destiny_flow}")
