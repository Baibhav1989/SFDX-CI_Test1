import shlex, subprocess, os
from PackageHasIsReleased import package_has_released
class sdfxcmd:
  
    sd1=package_has_released()
    xv1=sd1.runPackageList();
    print("\n success : ",xv1.success)
    print("\n validate : ",xv1.validate)
    print("\n data : ",xv1.data)
    if(xv1.validate==False):
        print("\n Package2Id : ",xv1.data["Package2Id"])