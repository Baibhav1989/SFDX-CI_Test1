import shlex, subprocess, os
from PackageHasIsReleased import package_has_released
class sdfxcmd:
  
    sd1=package_has_released()
    xv1=sd1.runPackageList();
    print("\n cmdsuccess : ",xv1.success)
    print("\n isReleased : ",xv1.validate)