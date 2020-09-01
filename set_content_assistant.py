from blip_session import BlipSession
import sys

if(len(sys.argv) < 5):
    print('Uso: python import_reports.py <chave_bot_origem> <chave_bot_destino>')
    exit()

first_bot_key = sys.argv[1] + ' ' + sys.argv[2]
second_bot_key = sys.argv[3] + ' ' + sys.argv[4]

first_bot_bs = BlipSession(first_bot_key)
second_bot_bs = BlipSession(second_bot_key)

get_intent_body = {
  "to": "postmaster@ai.msging.net",
  "method": "get",
  "uri": "/content"
}



bot_intentions = first_bot_bs.force_command(get_intent_body)

print(bot_intentions['resource'])
for intetion in bot_intentions['resource']['items']:
    print(intetion)
    response = second_bot_bs.force_command({
  "to": "postmaster@ai.msging.net",
  "method": "set",
  "uri": "/content",
  "type": "application/vnd.iris.ai.content-result+json",
  "resource": intetion                
})

