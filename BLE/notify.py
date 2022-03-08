from bluepy import btle

class MyDelegate(btle.DefaultDelegate):
    def __init__(self,params):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self,cHandle,data):
        print("handling notification...")
        print(self)
        print(cHandle)
        print(data)

p = btle.Peripheral('50:F1:4A:C7:AE:32')
p.setDelegate(MyDelegate(0))

while True:
    if p.waitForNotifications(1.0):
        continue
    print("waiting...")
