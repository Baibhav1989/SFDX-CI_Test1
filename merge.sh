#!/bin/bash
# printenv
echo '============================================================================'
WORKSPACE=$(pwd)
echo "merge.sh workspace=$WORKSPACE"

echo "Connecting to the HUB in master branch"
              echo "connect to the HUB"
              username="$sf_user$SFDC_PLATFORM_HUB"
              echo $username
              sfdx force:auth:jwt:grant --clientid $sfdx_client_id_hub --jwtkeyfile $main_dir/sfdx-intuit-private-key.key --username $username --setdefaultdevhubusername -a b2b-devhub --json

              echo "connect to beta and make alias"
              username="$sf_user$SFDC_PLATFORM_BETA"
              echo $username
              sfdx force:auth:jwt:grant --clientid $sfdx_client_id_beta --jwtkeyfile $main_dir/sfdx-intuit-private-key.key --username $username --instanceurl https://test.salesforce.com -a neworgbeta --json

              echo "create a version of the package"
              PackageVersionId=$(sfdx force:package:version:create -p EBS-SFDX-Package-1 -d force-app -k instKeyIntuit1234 --wait 10 -v b2b-devhub --json | jq '.result .SubscriberPackageVersionId')
              PackageVersionId=`echo $PackageVersionId | sed 's/^.\(.*\).$/\1/'`
              echo "PackageVersionId is here::"
              echo $PackageVersionId
              # run with JQ  -- sfdx force:package:version:create -p EBS-SFDX-Package-1 -d force-app -k instKeyIntuit1234 --wait 10 -v b2b-devhub --json | jq '.result .SubscriberPackageVersionId'                   
              scripts_dir=$main_dir/scripts
              echo $scripts_dir
              chgs_dir=$main_dir/changes
              echo $chgs_dir
              src_dir=$main_dir/changes/src
              echo $src_dir
              # find the changes using a script
              mkdir -p $src_dir/classes/
              ./scripts/find_chgs.sh
              changes=$(ls $src_dir/classes/)

              echo "install the package"
              sfdx force:package:install --wait 10 --publishwait 10 --package $PackageVersionId -k instKeyIntuit1234 -r -u neworgbeta -a package
              #EBS-SFDX-Package-1@0.1.0-1   -- need to replace with Id from above command 
              # echo "releasing the repo"
              # python scripts/release_repo.py

            #   echo "connect to the HUB"
            #   username="$sf_user$SFDC_PLATFORM_HUB"
            #   echo $username
            #   sfdx force:auth:jwt:grant --clientid $sfdx_client_id_hub --jwtkeyfile $main_dir/sfdx-intuit-private-key.key --username $username --setdefaultdevhubusername -a b2b-devhub --json

              echo "connect to e2e and make alias"
              username="$sf_user$SFDC_PLATFORM_E2E"
              echo $username
              sfdx force:auth:jwt:grant --clientid $sfdx_client_id_e2e --jwtkeyfile $main_dir/sfdx-intuit-private-key.key --username $username --instanceurl https://test.salesforce.com -a neworge2e --json

              echo "promote the package version"
              sfdx force:package:version:promote -p $PackageVersionId  -v b2b-devhub

              echo "install the package in e2e"
              sfdx force:package:install --wait 10 --publishwait 10 --package $PackageVersionId -k instKeyIntuit1234 -r -u neworge2e -a package
echo '----end merge section--------------------------------------------------'