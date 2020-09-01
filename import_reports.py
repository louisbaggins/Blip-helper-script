from blip_session import BlipSession
import sys
def get_reports(bot_session):
    get_reports_body = {
        "to": "postmaster@analytics.msging.net",
        "method": "get",
        "uri": "/reports"
    }

    reports = bot_session.force_command(get_reports_body)
    
    # print(reports)
    return reports['resource']['items']

def create_reports(bot_session, report):
    get_reports_body = {
        "to": "postmaster@analytics.msging.net",
        "method": "set",
        "uri": "/reports/",
        "type": "application/vnd.iris.report+json",
        "resource": report
    }
    response = bot_session.force_command(get_reports_body)
    print(response)

if(len(sys.argv) < 5):
    print('Uso: python import_reports.py <chave_bot_origem> <chave_bot_destino>')
    exit()

origin_bot_key = sys.argv[1] + ' ' + sys.argv[2]
destiny_bot_key = sys.argv[3] + ' ' + sys.argv[4]

origin_bot_session = BlipSession(origin_bot_key)
destiny_bot_session = BlipSession(destiny_bot_key)

destiny_bot_session.process_command
reports = get_reports(origin_bot_session)
for report in reports:
    create_reports(destiny_bot_session, report)