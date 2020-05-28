import shlex, subprocess, os
from SfdxJosnParser import SfdxJosnParser
class sdfxcmd:
   
    # command to run sfdx conamd in terminal and get response
    #command_line = "sfdx force:org:list --all --json"
    #process = subprocess.run(command_line, shell=True, stdout=subprocess.PIPE)
    #print ("output 2: ")
    #es_json_data=process.stdout.decode('utf-8')
    #print (res_json_data)
    
    #Command to open file and cread it data
    f = open("force_orglist.json", "r")
    res_json_data=f.read()
    print(res_json_data)
    sd=SfdxJosnParser()
    sd.parseJosn(res_json_data)

