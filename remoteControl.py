# -*- coding: iso-8859-1 -*-#
import winrm
import time
import subprocess, sys
import wmi

#Remote Machine Conf
hName = raw_input("Enter Host Name: ")
hID = raw_input("Enter user name: ")
hPW = raw_input("Enter password: ")

s = winrm.Session(hName, auth=(hID, hPW))
c = wmi.WMI(hName, user=hID, password=hPW)
#Reboot func
def remoteReboot():
    print "rebooting machine in 10 sec"
    s.run_cmd('shutdown -r')
    for i in xrange(10,0,-1):
        time.sleep(1)
        print i

#checkUpdate
def checkUpdate():
    p = subprocess.Popen(["powershell.exe",
                          "PathOfcheckUpdateScript\\checkUpdate.ps1"],
                         stdout=sys.stdout)
    p.communicate()

#serviceStatus func
def serviceStatus():
    p = subprocess.Popen(["powershell.exe",
                          "PathOfcredScript\\cred.ps1"],
                         stdout=sys.stdout)
    print "Remote machine service status"
    p.communicate()

#last loged on
def lastLogon():
    rmTime2 = s.run_cmd('net user ' + hID)
    print rmTime2.std_out #723-780

#last loged on2
def lastLog2():
    rmTime3 = s.run_cmd('quser')
    print rmTime3.std_out

#Check specific service status
def getServiceStatus(serviceName):
    for service in c.Win32_Service(name=serviceName):
        if (service.started):
            print "Status of " + service.name + ": Running"
        else:
            print "Status of " + service.name + ": Stopped"

#Services that are not running
def getStoppedServices():
    stopped_services = c.Win32_Service(State="Stopped")
    if stopped_services:
        for s in stopped_services:
            print s.Caption, "service is not running"

#Stop Service
def stopService(serviceName):
    for service in c.Win32_Service(Name=serviceName):
        result, = service.StopService()
        if result == 0:
            print "Service", service.Name, "stopped"
        else:
            print "Some problem"
        break
    else:
        print "Service not found"

#Start Service
def startService(serviceName):
    for service in c.Win32_Service(Name=serviceName):
        result, = service.StartService()
        if result == 0:
            print "Service", service.Name, "running"
        else:
            print "Some problem"
        break
    else:
        print "Service not found"

