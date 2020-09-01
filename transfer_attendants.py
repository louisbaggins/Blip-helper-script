from blip_session import BlipSession
def create_attendant_body(attendant):
    return{
        "identity": attendant['identity'],
        "teams": attendant['teams']
    }

def get_request_body(skip, take):
    return {
        "to": "postmaster@desk.msging.net",
        "method": "get",
        "uri": f"/attendants?$skip={skip}&$take={take}"
    }

def get_attendants():
    origin_bot_auth_key = '{{origin_bot_auth_key}}'
    origin_bot_session = BlipSession(origin_bot_auth_key)
    skip = 0
    take = 100
    attendants_response = origin_bot_session.force_command(get_request_body(skip, take))
    attendants = attendants_response['resource']['items']
    while attendants_response['resource']['total'] >= 100:     
        skip = 100
        take += 100
        attendants_response = origin_bot_session.force_command(get_request_body(skip, take))
        attendants += attendants_response['resource']['items']

    return attendants

def set_attendants(attendants):
    destiny_bot_auth_key = '{{destinity_auth_key}}'
    destiny_bot_session = BlipSession(destiny_bot_auth_key)
    for attendant in attendants:
        crb = {
            "to": "postmaster@desk.msging.net",
            "method": "set",
            "uri": "/attendants",
            "type": "application/vnd.iris.desk.attendant+json",
            "resource": create_attendant_body(attendant)
        }

        set_attendant_response = destiny_bot_session.force_command(crb, 3)
        if set_attendant_response['status'] == 'success':
            print(f'{attendant["fullname"]} adicionado com sucesso')
        else:
            print(f'Erro ao adicionar {attendant["fullname"]}')


attendants = get_attendants()
set_attendants(attendants)

