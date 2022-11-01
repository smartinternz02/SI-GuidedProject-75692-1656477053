#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "ttmy0h",
        "typeId": "plant",
        "deviceId":"123654"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if m=="pump ON":
        print("The pump is switched ON")
    else:
        print("The pump is switched OFF")

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,125)
    hum=random.randint(0,100)
    soilmoistLevel=random.randint(0,100)
    user=random.randint(0,10)
    if soilmoistLevel<65:
        print("Motor on")
    else:
        print("Motor off")
    myData={'temperature':temp, 'humidity':hum, 'soilmoistureLevel':soilmoistLevel, 'guest':user}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
