#!/bin/bash
# printenv
echo '============================================================================'
WORKSPACE=$(pwd)
echo "pr.sh workspace=$WORKSPACE"

echo "Connecting to the HUB in ANY OTHER EXCEPT MASTER branch"
          echo "connect to the HUB"
          username="$sf_user$SFDC_PLATFORM_HUB"
          echo $username
          sfdx force:auth:jwt:grant --clientid $sfdx_client_id_hub --jwtkeyfile $main_dir/sfdx-intuit-private-key.key --username $username --setdefaultdevhubusername -a b2b-devhub --json

          echo "connect to beta and make alias"
          username="$sf_user$SFDC_PLATFORM_BETA"
          echo $username
          sfdx force:auth:jwt:grant --clientid $sfdx_client_id_beta --jwtkeyfile $main_dir/sfdx-intuit-private-key.key --username $username --instanceurl https://test.salesforce.com -a neworgbeta --json

          echo "limit display to check current scratch org limits"
          sfdx force:limits:api:display -u b2b-devhub --json

          echo "create a scratch org"
          sfdx force:org:create --setdefaultusername --setalias sfdx-package-1 --definitionfile config/project-scratch-def.json --json

          echo "print list of all the setup you just did -- including scratch org"
          sfdx force:org:list --all --json

          echo "push the source to the new scratch org"
          sfdx force:source:push --json

          echo "deleting scratch org after use"
          sfdx force:org:delete -u sfdx-package-1 -p --json

          echo "limit display to check current scratch org limits"
          sfdx force:limits:api:display -u b2b-devhub --json
echo '----end pr section--------------------------------------------------'