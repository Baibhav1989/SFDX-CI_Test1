# developer name : Baibhav kumar
# Created Date : 26th May,2020
# purpose : to parse Josn and return josn as html table 

import json
class SfdxJosnParser:

    returnStr="<table>"
    #rowcount=1

    # methiod parseJosn 
    # takes Input json as string
    def parseJosn(self,josn_data):

        print("JSON : ",josn_data)
        strdata=json.loads(josn_data)

        for (k,v) in strdata.items():
            if (k=="status") and (v==0):
                if "result" in strdata.keys():
                    self.parseResultdata(strdata["result"])

        self.returnStr += "</table>"
        print("\n ****************  \n")
        print(self.returnStr,"\n")
        return self.returnStr;
                           
    # *** Method parseJosn End

    # methiod to parse result data 
    def parseResultdata(self,resultdata):
        print(resultdata)
        if isinstance(resultdata,list):

            print("\n trtewrewr***Yes**")
            self.parselistdata(resultdata)

        else:

            print("\n trtewrewr***No**")
            for (k1,v1) in resultdata.items():
                if isinstance(v1,list):
                    self.returnStr += "<tr><td><b>#</b></td><td><b>"+ str(k1) +"</b></td></tr>"
                    self.parselistdata(v1)

    # *** Method parseResultdata End

    # methiod to parse list data 
    def parselistdata(self,listdata):
        rowcount=1
        for l in listdata:
            self.returnStr += "<tr><td>"+ str(rowcount) +"</td><td>"
            rowcount=rowcount+1
            for (k,v) in l.items():                      
                if  isinstance(v,list):
                    self.returnStr +="<table>"
                    self.parselistdata(v)
                    self.returnStr +="</table>"
                else:
                    self.returnStr += str(k)+" : "+str(v)+"<br/>"
            self.returnStr +="</td></tr>"

    # *** Method parselistdata End        

                                                     
