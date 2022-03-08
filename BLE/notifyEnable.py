from bluepy import btle

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print("A notification was received: %s" %data)
        print(bytes(data))
        vbat = (data[0]<<8)+data[1]	# First two bytes battery voltage
        temp = (data[2]<<8)+data[3]	# Second two bytes temperature value
        print(vbat/1000.000)
        print(temp/100.00)
        
print("ASD")



p = btle.Peripheral('50:F1:4A:C7:AE:32') # Temp Pal MAC Address
p.setDelegate( MyDelegate() )

'''print("Device services list:")
for svc in p.services:
	print(str(svc))'''


# Setup to turn notifications on, e.g.
svc = p.getServiceByUUID('c050')		# Temp Pal Temperature & Battery Service UUID
ch = svc.getCharacteristics('c05a')[0]	# Temp Pal Temperature & Battery Characteristic UUID
print(ch.valHandle)

p.writeCharacteristic(ch.valHandle+1, b'\x01\x00') # To Enable Notifications

while True:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    print("Waiting...")
    # Perhaps do something else here
