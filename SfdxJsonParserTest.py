import unittest,shlex, subprocess
from SfdxJosnParser import SfdxJosnParser

class SfdxJsonParserTest(unittest.TestCase):
    def test_SDFX_Json(self):
        command_line = "sfdx force:org:list --all --json"
        process = subprocess.run(command_line, shell=True, stdout=subprocess.PIPE)
        print ("output 2: ")
        res_json_data=process.stdout.decode('utf-8')
        print (res_json_data)
        sd=SfdxJosnParser()
        xv = sd.parseJosn(res_json_data)
        self.assertEqual(xv.success,True)
        print("\n")
        print("Status : ",xv.success)
        print("\n Table HTML : \n \n",xv.resptbale)

    # python3 -m unittest SfdxJsonParserTest
        
        
    
