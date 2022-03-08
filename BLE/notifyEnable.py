from bluepy import btle

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print("A notification was received: %s" %data)
        print(bytes(data))
        temp = (data[0]<<8)+data[1]
        vbat = (data[2]<<8)+data[3]
        print(temp)
        print(vbat)
        
print("ASD")


p = btle.Peripheral('50:F1:4A:C7:AE:32')
p.setDelegate( MyDelegate() )

print("qwe")

print("Device services list:")
for svc in p.services:
	print(str(svc))


# Setup to turn notifications on, e.g.
svc = p.getServiceByUUID('c050')
ch = svc.getCharacteristics('c05a')[0]
print(ch.valHandle)

p.writeCharacteristic(ch.valHandle+1, b'\x01\x00')

while True:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    print("Waiting...")
    # Perhaps do something else here
