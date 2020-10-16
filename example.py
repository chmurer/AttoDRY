from PyAttoDRY import AttoDRY
import time

print('Connect to the AttoDRY')
AttoDRY.begin(setup_version=1)
AttoDRY.Connect(COMPort='COM4')

# you need to wait for initialization; if you just start sending
# commands, the connection will be lost.
time.sleep(10.0)

IN = AttoDRY.isDeviceInitialised()
CN = AttoDRY.isDeviceConnected()
# state that it is initialized and connected:
if IN==1 and CN ==1:
	print('The AttoDRY device is initialized and connected')
else:
	print('something went wrong.')


B = AttoDRY.getMagneticField()
T = AttoDRY.getSampleTemperature()

print('The current magnetic field is: '+str(B)+' T')
print('The current temeperature is: '+str(T)+' K')

time.sleep(1.0)

AttoDRY.setUserMagneticField(0.01)
time.sleep(0.1)
AttoDRY.setUserTemperature(1.9)

print('Both magnetic field and temperature have been set to new values. This will not change anything as long as field and temperature control are not toggled.')

time.sleep(2.0)

AttoDRY.toggleMagneticFieldControl()
time.sleep(0.1)
AttoDRY.toggleFullTemperatureControl()
print('toggled Temperature and field control.')


# always end by disconnect and end
AttoDRY.Disconnect()
AttoDRY.end()