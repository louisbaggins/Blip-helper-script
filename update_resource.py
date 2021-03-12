from blip_session import BlipSession


def get_resource_dict(bot_bs, resource_name):
    resource_value = bot_bs.force_command({
        "method": "get",
        "uri": f"/resources/{resource_name}"
    })

    return {resource_name: resource_value['resource']}


def get_all_resources(bot_bs, get_resource_rb):
    resources = bot_bs.force_command(get_resource_rb)
    return resources['resource']['items']


def set_resource(destiny_bot_bs, resource_dict):
    keys = [
        key
        for key in resource_dict.keys()
    ]
    for key in keys: 
        print(key)
        print(resource_dict[key])
        response = destiny_bot_bs.force_command({
            "method": "set",
            "uri": f"/resources/{key}",
            "type": "text/plain",
            "resource": resource_dict[key]
        })
        print(response)


bot_key = '{{origin_bot_key}}'
destiny_bot_key = '{{destiny_bot_key}}'
bot_bs = BlipSession(bot_key)
destiny_bot_bs = BlipSession(destiny_bot_key)

get_resource_rb = {
    "method": "get",
    "uri": "/resources/"
}

resources = get_all_resources(bot_bs, get_resource_rb)
resource_dict = dict()
resources_values = [
    get_resource_dict(bot_bs, resource_key)
    for resource_key in resources
]

for resource in resources_values:
    set_resource(destiny_bot_bs, resource)