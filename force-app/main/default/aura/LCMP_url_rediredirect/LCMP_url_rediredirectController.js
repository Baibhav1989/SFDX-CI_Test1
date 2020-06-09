({
    recordUpdated : function(component, event, helper) {
        var changeType = event.getParams().changeType;
        var recdata=component.get("v.recdData");
        if (changeType === "LOADED"){
            var navService = cmp.find("navService");
            var urlstr="https://google.com";
            // eg:  var urlstr="/login?"+recdData.name
            var pageReference={    
                "type": "standard__webPage",
                "attributes": {
                    "url": urlstr
                }
            };
            $A.get("e.force:closeQuickAction");
            navService.navigate(pageReference);
        }

    }
})
