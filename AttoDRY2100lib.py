# This is a Python script for direct control of the AttoDRY2100 cryostat.
# It depends on the .dll files provided by Attocube (AttoDRYLib.dll) which
# has to be referred to in the dll_directory variable. All functions
# are implemented in the given code, but not all functions are tested.
# You need to install the 2016 labview runtime engine. Additinally, the 
# script will only work with a 32 bit python version. 
#
# AttoDRY2100lib.py and PyAttoDRY2100.py are written by 
# Christoph Murer
# Magnetism and interface Physics, ETH Zurich
# christoph.murer@mat.ethz.ch or chmurer@gmail.com
# inspired by the ANC350 scrips written by Rob Heath and Brian Schaefer (https://github.com/Laukei/pyanc350)

# define the path to the AttoDRY DLL:
dll_directory = 'C:\\Program Files (x86)\\National Instruments\\LabVIEW 2020\\user.lib\\attoDRYLib\\'


import ctypes
import os
os.add_dll_directory(dll_directory)



# error code (EC) as described by 

EC_Ok = 0                      # No error
EC_Error = -1                  # Unknown / other error

#checks the errors returned from the dll
def checkError(code,func,args):
    if code == EC_Ok:
        return
    elif code <= EC_Error:             
        raise Exception("Error: unspecific in"+str(func.__name__)+"with parameters:"+str(args))
    else:                    
        raise Exception("Error: unknown Error code: "+str(code))
    return code


# load attoDRYLib...
attoDRYLib = ctypes.windll.attoDRYLib
#############################################################################################################
##### aliases for the DLL functions (only selected ones; we want to change field and temperature only):
#############################################################################################################

##### communication
getActionMessage = getattr(attoDRYLib,'AttoDRY_Interface_getActionMessage')
begin = getattr(attoDRYLib,'AttoDRY_Interface_begin')
Cancel = getattr(attoDRYLib,'AttoDRY_Interface_Cancel')
Confirm = getattr(attoDRYLib,'AttoDRY_Interface_Confirm')
Connect = getattr(attoDRYLib,'AttoDRY_Interface_Connect')
Main = getattr(attoDRYLib,'AttoDRY_Interface_Main')
Disconnect = getattr(attoDRYLib,'AttoDRY_Interface_Disconnect')
end = getattr(attoDRYLib,'AttoDRY_Interface_end')
getAttodryErrorMessage = getattr(attoDRYLib,'AttoDRY_Interface_getAttodryErrorMessage')
getAttodryErrorStatus = getattr(attoDRYLib,'AttoDRY_Interface_getAttodryErrorStatus')
goToBaseTemperature = getattr(attoDRYLib,'AttoDRY_Interface_goToBaseTemperature')
lowerError = getattr(attoDRYLib,'AttoDRY_Interface_lowerError')
LVDLLStatus = getattr(attoDRYLib,'LVDLLStatus')
startLogging = getattr(attoDRYLib,'AttoDRY_Interface_startLogging')
startSampleExchange = getattr(attoDRYLib,'AttoDRY_Interface_startSampleExchange')
stopLogging = getattr(attoDRYLib,'AttoDRY_Interface_stopLogging')
sweepFieldToZero = getattr(attoDRYLib,'AttoDRY_Interface_sweepFieldToZero')
downloadSampleTemperatureSensorCalibrationCurve = getattr(attoDRYLib,'AttoDRY_Interface_downloadSampleTemperatureSensorCalibrationCurve')
downloadTemperatureSensorCalibrationCurve = getattr(attoDRYLib,'AttoDRY_Interface_downloadTemperatureSensorCalibrationCurve')
uploadSampleTemperatureCalibrationCurve = getattr(attoDRYLib,'AttoDRY_Interface_uploadSampleTemperatureCalibrationCurve')
uploadTemperatureCalibrationCurve = getattr(attoDRYLib,'AttoDRY_Interface_uploadTemperatureCalibrationCurve')

##### asking questions
isControllingField = getattr(attoDRYLib,'AttoDRY_Interface_isControllingField')
isControllingTemperature = getattr(attoDRYLib,'AttoDRY_Interface_isControllingTemperature')
isDeviceConnected = getattr(attoDRYLib,'AttoDRY_Interface_isDeviceConnected')
isDeviceInitialised = getattr(attoDRYLib,'AttoDRY_Interface_isDeviceInitialised')
isGoingToBaseTemperature = getattr(attoDRYLib,'AttoDRY_Interface_isGoingToBaseTemperature')
isExchangeHeaterOn = getattr(attoDRYLib,'AttoDRY_Interface_isExchangeHeaterOn')
isPersistentModeSet = getattr(attoDRYLib,'AttoDRY_Interface_isPersistentModeSet')
isPumping = getattr(attoDRYLib,'AttoDRY_Interface_isPumping')
isSampleExchangeInProgress = getattr(attoDRYLib,'AttoDRY_Interface_isSampleExchangeInProgress')
isSampleHeaterOn = getattr(attoDRYLib,'AttoDRY_Interface_isSampleHeaterOn')
isSampleReadyToExchange = getattr(attoDRYLib,'AttoDRY_Interface_isSampleReadyToExchange')
isSystemRunning = getattr(attoDRYLib,'AttoDRY_Interface_isSystemRunning')
isPumping = getattr(attoDRYLib,'AttoDRY_Interface_isPumping')
isZeroingField = getattr(attoDRYLib,'AttoDRY_Interface_isZeroingField')

##### queries
queryReservoirTsetColdSample = getattr(attoDRYLib,'AttoDRY_Interface_queryReservoirTsetColdSample') 
queryReservoirTsetWarmMagnet = getattr(attoDRYLib,'AttoDRY_Interface_queryReservoirTsetWarmMagnet')
queryReservoirTsetWarmSample = getattr(attoDRYLib,'AttoDRY_Interface_queryReservoirTsetWarmSample')
querySampleHeaterMaximumPower = getattr(attoDRYLib,'AttoDRY_Interface_querySampleHeaterMaximumPower')
querySampleHeaterResistance = getattr(attoDRYLib,'AttoDRY_Interface_querySampleHeaterResistance')
querySampleHeaterWireResistance = getattr(attoDRYLib,'AttoDRY_Interface_querySampleHeaterWireResistance')

##### toggle commands
toggleCryostatInValve = getattr(attoDRYLib,'AttoDRY_Interface_toggleCryostatInValve')
toggleCryostatOutValve = getattr(attoDRYLib,'AttoDRY_Interface_toggleCryostatOutValve')
toggleDumpInValve = getattr(attoDRYLib,'AttoDRY_Interface_toggleDumpInValve')
toggleDumpOutValve = getattr(attoDRYLib,'AttoDRY_Interface_toggleDumpOutValve')
toggleExchangeHeaterControl = getattr(attoDRYLib,'AttoDRY_Interface_toggleExchangeHeaterControl')
toggleFullTemperatureControl = getattr(attoDRYLib,'AttoDRY_Interface_toggleFullTemperatureControl')
toggleHeliumValve = getattr(attoDRYLib,'AttoDRY_Interface_toggleHeliumValve')
toggleInnerVolumeValve = getattr(attoDRYLib,'AttoDRY_Interface_toggleInnerVolumeValve')
toggleOuterVolumeValve = getattr(attoDRYLib,'AttoDRY_Interface_toggleOuterVolumeValve')
toggleMagneticFieldControl = getattr(attoDRYLib,'AttoDRY_Interface_toggleMagneticFieldControl')
togglePersistentMode = getattr(attoDRYLib,'AttoDRY_Interface_togglePersistentMode')
togglePump = getattr(attoDRYLib,'AttoDRY_Interface_togglePump')
togglePumpValve = getattr(attoDRYLib,'AttoDRY_Interface_togglePumpValve')
toggleSampleTemperatureControl = getattr(attoDRYLib,'AttoDRY_Interface_toggleSampleTemperatureControl') 
toggleStartUpShutdown = getattr(attoDRYLib,'AttoDRY_Interface_toggleStartUpShutdown') 

##### get values
getCryostatInPressure = getattr(attoDRYLib,'AttoDRY_Interface_getCryostatInPressure')
getCryostatInValve = getattr(attoDRYLib,'AttoDRY_Interface_getCryostatInValve')
getCryostatOutPressure = getattr(attoDRYLib,'AttoDRY_Interface_getCryostatOutPressure')
getCryostatOutValve = getattr(attoDRYLib,'AttoDRY_Interface_getCryostatOutValve')
getDumpInValve = getattr(attoDRYLib,'AttoDRY_Interface_getDumpInValve')
getDumpOutValve = getattr(attoDRYLib,'AttoDRY_Interface_getDumpOutValve')
getDumpPressure = getattr(attoDRYLib,'AttoDRY_Interface_getDumpPressure')
getHeliumValve = getattr(attoDRYLib,'AttoDRY_Interface_getHeliumValve')
getInnerVolumeValve = getattr(attoDRYLib,'AttoDRY_Interface_getInnerVolumeValve')
getOuterVolumeValve = getattr(attoDRYLib,'AttoDRY_Interface_getOuterVolumeValve')
getReservoirHeaterPower = getattr(attoDRYLib,'AttoDRY_Interface_getReservoirHeaterPower')
getReservoirTemperature = getattr(attoDRYLib,'AttoDRY_Interface_getReservoirTemperature')
getReservoirTsetColdSample = getattr(attoDRYLib,'AttoDRY_Interface_getReservoirTsetColdSample')
getReservoirTsetWarmMagnet = getattr(attoDRYLib,'AttoDRY_Interface_getReservoirTsetWarmMagnet')
getReservoirTsetWarmSample = getattr(attoDRYLib,'AttoDRY_Interface_getReservoirTsetWarmSample')
getPressure = getattr(attoDRYLib,'AttoDRY_Interface_getPressure')
get40KStageTemperature = getattr(attoDRYLib,'AttoDRY_Interface_get40KStageTemperature')
get4KStageTemperature = getattr(attoDRYLib,'AttoDRY_Interface_get4KStageTemperature')
getDerivativeGain = getattr(attoDRYLib,'AttoDRY_Interface_getDerivativeGain')
getIntegralGain = getattr(attoDRYLib,'AttoDRY_Interface_getIntegralGain')
getMagneticField = getattr(attoDRYLib,'AttoDRY_Interface_getMagneticField')
getMagneticFieldSetPoint = getattr(attoDRYLib,'AttoDRY_Interface_getMagneticFieldSetPoint')
getProportionalGain = getattr(attoDRYLib,'AttoDRY_Interface_getProportionalGain')
getSampleHeaterMaximumPower = getattr(attoDRYLib,'AttoDRY_Interface_getSampleHeaterMaximumPower')
getSampleHeaterPower = getattr(attoDRYLib,'AttoDRY_Interface_getSampleHeaterPower')
getSampleHeaterResistance = getattr(attoDRYLib,'AttoDRY_Interface_getSampleHeaterResistance')
getSampleHeaterWireResistance = getattr(attoDRYLib,'AttoDRY_Interface_getSampleHeaterWireResistance')
getSampleTemperature = getattr(attoDRYLib,'AttoDRY_Interface_getSampleTemperature')
getUserTemperature = getattr(attoDRYLib,'AttoDRY_Interface_getUserTemperature')
getVtiHeaterPower = getattr(attoDRYLib,'AttoDRY_Interface_getVtiHeaterPower')
getVtiTemperature = getattr(attoDRYLib,'AttoDRY_Interface_getVtiTemperature')
getPumpValve = getattr(attoDRYLib,'AttoDRY_Interface_getPumpValve')
getTurbopumpFrequency = getattr(attoDRYLib,'AttoDRY_Interface_getTurbopumpFrequency')

##### set values
setDerivativeGain = getattr(attoDRYLib,'AttoDRY_Interface_setDerivativeGain')
setIntegralGain = getattr(attoDRYLib,'AttoDRY_Interface_setIntegralGain')
setProportionalGain = getattr(attoDRYLib,'AttoDRY_Interface_setProportionalGain')
setReservoirTsetColdSample = getattr(attoDRYLib,'AttoDRY_Interface_setReservoirTsetColdSample')
setReservoirTsetWarmMagnet = getattr(attoDRYLib,'AttoDRY_Interface_setReservoirTsetWarmMagnet')
setReservoirTsetWarmSample = getattr(attoDRYLib,'AttoDRY_Interface_setReservoirTsetWarmSample')
setSampleHeaterMaximumPower = getattr(attoDRYLib,'AttoDRY_Interface_setSampleHeaterMaximumPower')
setSampleHeaterPower = getattr(attoDRYLib,'AttoDRY_Interface_setSampleHeaterPower')
setSampleHeaterResistance = getattr(attoDRYLib,'AttoDRY_Interface_setSampleHeaterResistance')
setSampleHeaterWireResistance = getattr(attoDRYLib,'AttoDRY_Interface_setSampleHeaterWireResistance')
setUserMagneticField = getattr(attoDRYLib,'AttoDRY_Interface_setUserMagneticField')
setUserTemperature = getattr(attoDRYLib,'AttoDRY_Interface_setUserTemperature')
setVTIHeaterPower = getattr(attoDRYLib,'AttoDRY_Interface_setVTIHeaterPower')



#############################################################################################################
##### error checking and handling...
#############################################################################################################

##### communication
getActionMessage.errcheck = checkError
begin.errcheck = checkError
Cancel.errcheck = checkError
Confirm.errcheck = checkError
Connect.errcheck = checkError
Main.errcheck = checkError
Disconnect.errcheck = checkError
end.errcheck = checkError
getAttodryErrorMessage.errcheck = checkError
getAttodryErrorStatus.errcheck = checkError
goToBaseTemperature.errcheck = checkError
lowerError.errcheck = checkError
startLogging.errcheck = checkError
startSampleExchange.errcheck = checkError
stopLogging.errcheck = checkError
sweepFieldToZero.errcheck = checkError
downloadSampleTemperatureSensorCalibrationCurve.errcheck = checkError
downloadTemperatureSensorCalibrationCurve.errcheck = checkError
uploadSampleTemperatureCalibrationCurve.errcheck = checkError
uploadTemperatureCalibrationCurve.errcheck = checkError
LVDLLStatus.errcheck = checkError

##### asking questions
isControllingField.errcheck = checkError
isControllingTemperature.errcheck = checkError
isDeviceConnected.errcheck = checkError
isDeviceInitialised.errcheck = checkError
isGoingToBaseTemperature.errcheck = checkError
isExchangeHeaterOn.errcheck = checkError
isPersistentModeSet.errcheck = checkError
isPumping.errcheck = checkError
isSampleExchangeInProgress.errcheck = checkError
isSampleHeaterOn.errcheck = checkError
isSampleReadyToExchange.errcheck = checkError
isSystemRunning.errcheck = checkError
isPumping.errcheck = checkError
isZeroingField.errcheck = checkError

##### queries
queryReservoirTsetColdSample.errcheck = checkError 
queryReservoirTsetWarmMagnet.errcheck = checkError
queryReservoirTsetWarmSample.errcheck = checkError
querySampleHeaterMaximumPower.errcheck = checkError
querySampleHeaterResistance.errcheck = checkError
querySampleHeaterWireResistance.errcheck = checkError

##### toggle commands
toggleCryostatInValve.errcheck = checkError
toggleCryostatOutValve.errcheck = checkError
toggleDumpInValve.errcheck = checkError
toggleDumpOutValve.errcheck = checkError
toggleExchangeHeaterControl.errcheck = checkError
toggleFullTemperatureControl.errcheck = checkError
toggleHeliumValve.errcheck = checkError
toggleInnerVolumeValve.errcheck = checkError
toggleOuterVolumeValve.errcheck = checkError
toggleMagneticFieldControl.errcheck = checkError
togglePersistentMode.errcheck = checkError
togglePump.errcheck = checkError
togglePumpValve.errcheck = checkError
toggleSampleTemperatureControl.errcheck = checkError
toggleStartUpShutdown.errcheck = checkError

##### get values
getCryostatInPressure.errcheck = checkError
getCryostatInValve.errcheck = checkError
getCryostatOutPressure.errcheck = checkError
getCryostatOutValve.errcheck = checkError
getDumpInValve.errcheck = checkError
getDumpOutValve.errcheck = checkError
getDumpPressure.errcheck = checkError
getHeliumValve.errcheck = checkError
getInnerVolumeValve.errcheck = checkError
getOuterVolumeValve.errcheck = checkError
getReservoirHeaterPower.errcheck = checkError
getReservoirTemperature.errcheck = checkError
getReservoirTsetColdSample.errcheck = checkError
getReservoirTsetWarmMagnet.errcheck = checkError
getReservoirTsetWarmSample.errcheck = checkError
getPressure.errcheck = checkError
get40KStageTemperature.errcheck = checkError
get4KStageTemperature.errcheck = checkError
getDerivativeGain.errcheck = checkError
getIntegralGain.errcheck = checkError
getMagneticField.errcheck = checkError
getMagneticFieldSetPoint.errcheck = checkError
getProportionalGain.errcheck = checkError
getSampleHeaterMaximumPower.errcheck = checkError
getSampleHeaterPower.errcheck = checkError
getSampleHeaterResistance.errcheck = checkError
getSampleHeaterWireResistance.errcheck = checkError
getSampleTemperature.errcheck = checkError
getUserTemperature.errcheck = checkError
getVtiHeaterPower.errcheck = checkError
getVtiTemperature.errcheck = checkError
getPumpValve.errcheck = checkError
getTurbopumpFrequency.errcheck = checkError

##### set values
setDerivativeGain.errcheck = checkError
setIntegralGain.errcheck = checkError
setProportionalGain.errcheck = checkError
setReservoirTsetColdSample.errcheck = checkError
setReservoirTsetWarmMagnet.errcheck = checkError
setReservoirTsetWarmSample.errcheck = checkError
setSampleHeaterMaximumPower.errcheck = checkError
setSampleHeaterPower.errcheck = checkError
setSampleHeaterResistance.errcheck = checkError
setSampleHeaterWireResistance.errcheck = checkError
setUserMagneticField.errcheck = checkError
setUserTemperature.errcheck = checkError
setVTIHeaterPower.errcheck = checkError
