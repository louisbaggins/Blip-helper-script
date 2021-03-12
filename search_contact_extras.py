from blip_session import BlipSession

AUTH_KEY = '{{bot_key}}'
SEARCHED_VALUE = '{{searched_value}}'
bs = BlipSession(AUTH_KEY, '{{organization}}') #Organization is optional#
searched_key = '{{searched_key}}'

def get_contact_crb(skip, take):
    return {
        "method" : "get",
        "uri" : f"/contacts?$skip={skip}&$take={take}"
    }

skip = 0
take = 100
response = bs.force_command(get_contact_crb(skip, take))
contact_found = False
while skip < response['resource']['total']:
    for contact in response['resource']['items']:
        if 'extras' in contact and searched_key in contact['extras'] and contact['extras'][searched_key] == SEARCHED_VALUE:
            print(f"Valor encontrado em {contact['identity']}")
            contact_found = True
    if contact_found:
        break
    skip += 100
    print(f'{skip} contatos analisados!')
    response = bs.force_command(get_contact_crb(skip, take))

if contact_found == False:
    print('Valor não encontrado nos contatos')