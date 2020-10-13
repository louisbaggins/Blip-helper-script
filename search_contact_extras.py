from blip_session import BlipSession

def get_contact_crb(skip, take):
    return {
        "method" : "get",
        "uri" : f"/contacts?$skip={skip}&$take={take}"
    }

AUTH_KEY = '{{bot_auth_key}}'
SEARCHED_VALUE = '{{searched_value}}'
bs = BlipSession(AUTH_KEY)

response = bs.force_command(get_contact_crb(0, 100))
skip = 0
take = 100
contact_found = False
while skip < response['resource']['total']:
    for contact in response['resource']['items']:
        if 'extras' in contact and 'CPF' in contact['extras'] and contact['extras']['CPF'] == SEARCHED_VALUE:
            print(f"Valor encontrado em {contact['identity']}")
            contact_found = True
    if contact_found:
        break
    skip += 100
    print(f'{skip} contatos analisados!')
    response = bs.force_command(get_contact_crb(skip, take))

if contact_found == False:
    print('Valor não encontrado nos contatos')