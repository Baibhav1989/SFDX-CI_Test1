import shlex, subprocess, os,json
class Wrapper(object):
    def __init__(self, cmdSuccess ,isReleased):
        self.success=cmdSuccess
        self.validate=isReleased

class package_has_released:

    def runPackageList(self):
        # command to run sfdx conamd in terminal and get response
        command_line = "sfdx force:package:version:list --json"
        process = subprocess.run(command_line, shell=True, stdout=subprocess.PIPE)
        print ("output 2: ")
        josn_data=process.stdout.decode('utf-8')
        print (josn_data)
        strdata=json.loads(josn_data)
        cmdsuccess=False
        isReleased=True
        for (k,v) in strdata.items():
            if (k=="status"):
                if (v==0):
                    cmdsuccess=True
                    if "result" in strdata.keys():
                        isReleased=self.parseResultdata(strdata["result"])
                elif (v==1):
                    cmdsuccess=False
        return Wrapper(cmdsuccess,isReleased)   
                    

    def parseResultdata(self,resultdata):
        if (isinstance(resultdata,list)): 
            for l in resultdata:
                 for (k,v) in l.items():
                     if(k=="IsReleased"):
                        if(v==True):               
                          return False
                          break
        return True            

        