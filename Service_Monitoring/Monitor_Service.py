import psutil
#
# Python Script to Check if...
# Windows Service is found|installed,stopped|running without pywin32
# Found at https://stackoverflow.com/questions/33843024
# Update to work on python 3.x
#


def getService(name):

    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))
    return service

service = getService('LanmanServer')
print(service)

if service:
    print("service found")
else:
    print("service not found")


if service and service['status'] == 'running':
    print("service is running")
else:
    print("service is not running")
