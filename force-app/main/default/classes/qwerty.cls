/************************************************************************************
  Author : Niharika Jaiswal(Altimetrik)
  Date   : 8th June 2020
  Purpose: This component is used for Approve Actuals button on SIP Scorecard object.
*************************************************************************************/
public class SIP_ApproveActuals {
    public static String groupMemberName ='SIP Admin';
    public static String Year ='2018';
    public static String actualsApproved ='Actuals Approved';
    public static String managerOrSIpAdminCanApproveMessage = 'Only the manager or SIP Admin can approve objectives';
    public static String priorValue= 'Prior to approving the actuals you must enter the actual performance for each objective';
   
    //Wrapper class
    public  class wrapApproveActuals {
        @AuraEnabled
        public boolean showAlert{get;set;} //Used to check alert
        public string alertMessage{get;set;} //Used to display alertMessage
    }
   
    @AuraEnabled
    public static wrapApproveActuals getData(String recId) {
       wrapApproveActuals wap = new wrapApproveActuals();
        //Declare list for SIP Scorecard
        List<SIP_ScoreCard__c> sipScore = new List<SIP_ScoreCard__c>();
        //Query for SIP Scorecard
        sipScore =[Select Id,Manager_NetworkID__c,SIP_ScoreObj_Locked__c,Year__c FROM SIP_ScoreCard__c WHERE ID =:recId];
        //Declare list for User
        List<User> userList =new List<User>();
        //Query for User
        userList =[Select Id,EmployeeNumber FROM User WHERE Id =:UserInfo.getUserId()];
        // Declare List for GroupMember
        List<GroupMember> groupM =new List<GroupMember>();
        //Check userList is not empty,then enter in the loop
        if(!userList.isEmpty()) {
            //Query for the groupMember
          groupM =[SELECT ID,GroupID,Group.Name,UserOrGroupId FROM GroupMember WHERE Group.Name =:groupMemberName and UserOrGroupId =:userList[0].Id LIMIT 1];
            if(!groupM.isEmpty() || ((sipScore[0].Manager_NetworkID__c) == (userList[0].EmployeeNumber))) {
                //Declare List for SIP_Objective__c
                List<SIP_Objective__c> sipObjective = new List<SIP_Objective__c>();
                //Query for the SIP_Objective__c
                sipObjective =[SELECT Id FROM SIP_Objective__c where SIP_ScoreCard_New__c =:recId and ((Actual_Performance__c = Null and Enable_Exception_Management__c = False) or (Enable_Exception_Management__c = True and Exc_Amount__c = Null))];
                //Check sipObjective List is empty
                if(sipObjective.isEmpty()) {
                    SIP_ScoreCard__c sipScoreCard = new SIP_ScoreCard__c();
                    sipScoreCard.Id = recId;
                    sipScoreCard.SIP_Scorecard_Status__c = actualsApproved;
                    update sipScoreCard; //Update SIP_ScoreCard__c
                    wap.showAlert = false; //Set the boolean to false
                    List<SIP_Objective__c> sipObj = new List <SIP_Objective__c>();
                    sipObj =[SELECT Id FROM SIP_Objective__c where SIP_ScoreCard_New__c =:recId];
                    //Assigning the value to IsLocked String
                    String IsLocked = sipObj[0].SIP_ScoreObj_Locked__c;
                    //Check sipObjective List is not empty
                    if(!sipObjective.isEmpty()) {
                        for(SIP_Objective__c sp:sipObj){
                            //Check if IsLocked value is 1
                            if(IsLocked =='1') {
                                SIP_Objective__c obj=new SIP_Objective__c();
                                obj.Id = sp.Id;
                                obj.RecordTypeId ='0122A000001MNKVQA4';
                                 
                            }
                            //Check if IsLocked value is 0
                            if(IsLocked =='0') {
                               SIP_Objective__c obj=new SIP_Objective__c();
                               obj.Id = sp.Id;
                                //Check for 2018 year
                                if(sipScore[0].Year__c == Year) {
                                  obj.RecordTypeId ='0122A000001F6cI';
                                }
                                else {
                                    obj.RecordTypeId ='0122A000001MNKWQA4';
                                }
                                sipObj.add(obj);
                            }
                        }
                        update sipObj;
                    }
                   
                }
                //Check for else condition
                else {
                     wap.showAlert = true;
                     wap.alertMessage =priorValue;
                }
            }
            else {
                wap.showAlert = true;
                wap.alertMessage =managerOrSIpAdminCanApproveMessage;
            }  
        }
        //Return wap
        return wap;  
    }
}