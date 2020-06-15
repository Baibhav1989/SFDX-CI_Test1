import shlex, subprocess, os,json
class Wrapper(object):
    def __init__(self, cmdSuccess ,isReleased,data):
        self.success=cmdSuccess
        self.validate=isReleased
        self.data=data
        
class package_has_released:

    def runPackageList(self):
        # command to run sfdx conamd in terminal and get response
       
        command_line = "sfdx force:package:version:list --json"
        process = subprocess.run(command_line, shell=True, stdout=subprocess.PIPE)
        print ("output 2: ")
        josn_data=process.stdout.decode('utf-8')

        '''
        Sample JSON :

            {
            "status": 0,
            "result": [
                {
                    "Package2Id": "0Ho2v000000PB99CAG",
                    "Branch": null,
                    "Tag": null,
                    "MajorVersion": 0,
                    "MinorVersion": 1,
                    "PatchVersion": 0,
                    "BuildNumber": 1,
                    "Id": "05i2v000000Kz5CAAS",
                    "SubscriberPackageVersionId": "04t2v000007Ca2rAAC",
                    "Name": "ver 0.1",
                    "NamespacePrefix": null,
                    "Package2Name": "bonyUnPack",
                    "Description": null,
                    "Version": "0.1.0.1",
                    "IsPasswordProtected": true,
                    "IsReleased": false,
                    "CreatedDate": "2020-06-15 09:03",
                    "LastModifiedDate": "2020-06-15 09:03",
                    "InstallUrl": "https://login.salesforce.com/packaging/installPackage.apexp?p0=04t2v000007Ca2rAAC",
                    "CodeCoverage": "Data unavailable",
                    "HasPassedCodeCoverageCheck": "Data unavailable",
                    "ValidationSkipped": false,
                    "AncestorId": "N/A",
                    "AncestorVersion": "N/A",
                    "Alias": "bonyUnPack@0.1.0-1"
                    },
                    {
                    "Package2Id": "0Ho2v000000PB99CAG",
                    "Branch": null,
                    "Tag": null,
                    "MajorVersion": 0,
                    "MinorVersion": 1,
                    "PatchVersion": 0,
                    "BuildNumber": 2,
                    "Id": "05i2v000000Kz5HAAS",
                    "SubscriberPackageVersionId": "04t2v000007Ca2wAAC",
                    "Name": "ver 0.1",
                    "NamespacePrefix": null,
                    "Package2Name": "bonyUnPack",
                    "Description": null,
                    "Version": "0.1.0.2",
                    "IsPasswordProtected": true,
                    "IsReleased": true,
                    "CreatedDate": "2020-06-15 09:06",
                    "LastModifiedDate": "2020-06-15 09:06",
                    "InstallUrl": "https://login.salesforce.com/packaging/installPackage.apexp?p0=04t2v000007Ca2wAAC",
                    "CodeCoverage": "Data unavailable",
                    "HasPassedCodeCoverageCheck": "Data unavailable",
                    "ValidationSkipped": false,
                    "AncestorId": "N/A",
                    "AncestorVersion": "N/A",
                    "Alias": "bonyUnPack@0.1.0-2"
                    }
                ]
            }

        '''
        print (josn_data)
        strdata=json.loads(josn_data)
        cmdsuccess=False
        isReleased=None
        for (k,v) in strdata.items():
            if (k=="status"):
                if (v==0):
                    cmdsuccess=True
                    if "result" in strdata.keys():
                        isReleased=self.parseResultdata(strdata["result"])
                elif (v==1):
                    cmdsuccess=False
        return Wrapper(cmdsuccess,isReleased.validate,isReleased.data)   
                    

    def parseResultdata(self,resultdata):
        if (isinstance(resultdata,list)): 
            for l in resultdata:
                loopbreak=False
                data={}
                for (k,v) in l.items():
                    if(k=="IsReleased"):
                        if(v==True):               
                            loopbreak=True
                    else:
                         data[k]=v       
                           
                if(loopbreak):
                      print("\n DATA : ",data) 
                      return Wrapper(True,False,data)                  
                          
        return Wrapper(True,True,None)            

        