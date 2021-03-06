# developer name : Baibhav kumar
# Created Date : 26th May,2020
# purpose : to parse Josn and return josn as html table 

import json

class Wrapper(object):
    def __init__(self, cmdSuccess ,tablestring):
        self.success=cmdSuccess
        self.resptbale=tablestring

class SfdxJosnParser:
  

    returnStr="<table>"
    #rowcount=1

    # methiod parseJosn 
    # takes Input json as string
    def parseJosn(self,josn_data):

        print("JSON : ",josn_data)
        strdata=json.loads(josn_data)
        cmdsuccess=False
        for (k,v) in strdata.items():
            if (k=="status"):
                if (v==0):
                    cmdsuccess=True
                    self.returnStr += "<tr><td><b>STATUS</b></td><td><b>SUCCESS</b></td></tr>"
                    if "result" in strdata.keys():
                        self.parseResultdata(strdata["result"])
                elif (v==1):
                    cmdsuccess=False
                    self.returnStr += "<tr><td><b>STATUS</b></td><td><b>FAILED</b></td></tr>"
                    self.parseErrordata(strdata)

        self.returnStr += "</table>"       
        #return wapper
        return Wrapper(cmdsuccess,self.returnStr)
         
                           
    # *** Method parseJosn End


    # methiod to parse result data 
    def parseResultdata(self,resultdata):
        i=1
        print(resultdata)

        if (isinstance(resultdata,list)):

            self.parselistdata(resultdata)

        else:

            for (k,v) in resultdata.items():
                if isinstance(v,list):
                    self.returnStr += "<tr><td><b>#</b></td><td><b>"+ str(k) +"</b></td></tr>"
                    self.parselistdata(v)
                else:
                    self.returnStr += "<tr><td>"+str(i)+"</td><td>"+str(k)+" : "+str(v) +"</td></tr>"
                    #self.returnStr += "<tr><td>"+str(i)+"</td><td><table><tr><td>"+str(k)+"</td><td>"+str(v)+"</td></tr></table></td></tr>"
                i=i+1   

    # *** Method parseResultdata End


    # methiod to parse list data 
    def parselistdata(self,listdata):
        rowcount=1
        for l in listdata:
            self.returnStr += "<tr><td>"+ str(rowcount) +"</td><td>"
            rowcount=rowcount+1
            for (k,v) in l.items():                      
                if (isinstance(v,list)):
                    self.returnStr +="<table>"
                    self.parselistdata(v)
                    self.returnStr +="</table>"
                else:
                    self.returnStr += str(k)+" : "+str(v)+"<br/>"
                    #self.returnStr += "<table><tr><td>"+str(k)+"</td><td>"+str(v)+"</td></tr></table>"
            self.returnStr +="</td></tr>"

    # *** Method parselistdata End 


    # methiod to parse Error data 
    def parseErrordata(self,errordata):
        for (k,v) in errordata.items():
            if (k != "status"):
                if(k=="name"):       
                    self.returnStr += "<tr><td><b>#</b></td><td><b>"+ str(v) +"</b></td></tr>"
                else:
                    if (not(isinstance(v,list))):
                        self.returnStr += "<tr><td><b>#</b></td><td><b>"+ str(k)+" : "+str(v) +"</b></td></tr>"
                    else:
                        self.parselistdata(v)    

                       
                                                     

