# Cloud Challenge

## Welcome

To register for a chance to win a prize, deploy your Python function with Cloud Functions. This should only take a few minutes...

In all cases, make sure to sign in with the provided account. The account on your Cloud Challenge card has the following format:
- devstar7xxx@gcplab.me

1. Open this tutorial in Cloud Shell
   - [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FPicardParis%2Fep22&cloudshell_tutorial=README.md)
2. Check that you're correctly signed in: 
   ```sh
   echo $USER
   ```
3. If you get a user of the following format, you're all good and you can move to the next step:
   ```terminal
   devstar7xxx
   ```
4. Otherwise, sign out from your existing account, manually sign in with the provided account, and launch the following command from Cloud Shell:
   ```sh
   cloudshell_open --repo_url "https://github.com/PicardParis/ep22" --tutorial "README.md" --force_new_clone
   ```

Note: For all commands to be launched in Cloud Shell, click the <walkthrough-cloud-shell-icon></walkthrough-cloud-shell-icon> button and the command will automatically be pasted.

## Project

1. Select the project pregenerated with your card account (do not create a new project):
   - <walkthrough-project-setup billing></walkthrough-project-setup>
2. Here is the currently selected project ID:
   - <walkthrough-project-id/>
3. It must have the following format:
   - europython22dub-7xxx
4. Run the following command from Cloud Shell to make it your current project:
   ```sh
   gcloud config set project <walkthrough-project-id/>
   ```

## APIs

Run the following command from Cloud Shell to enable the Cloud Functions and Cloud Build APIs:
```sh
gcloud services enable \
  cloudfunctions.googleapis.com \
  cloudbuild.googleapis.com
```
Note: Cloud Build is called by Cloud Functions to build your code into a container image.

## Code

1. Here is the workflow chosen for this Cloud Challenge:
   - An HTTP request triggers your Python function.
   - The function returns a JSON response with your Cloud Challenge data.
2. The skeleton of the Python function you're going to deploy is the following:
   ```py
   def cloud_challenge_data(request: flask.Request) -> flask.Response:
       """Cloud Function returning your Cloud Challenge data."""
       ...
       return flask.jsonify(data)
   ```
3. Open the file <walkthrough-editor-open-file filePath="src/main.py">`src/main.py`</walkthrough-editor-open-file> and edit your data  from the Cloud Shell Editor:
   ```py
      ...
      # 2. Your current status (pick one emoji)
      STATUS = "🚀"  # 🚀👍🥰🎉🔴🟠🟡🟢🔵
      # 3. Name on your badge
      NAME = "Siobhán Fáilte"
      # 4. Order number on your badge (5 Alpha-numeric chars in bottom-left corner)
      ORDER_NUMBER = "XXXXX"
      ...
   ```
4. Wait a couple of seconds for the file to be auto-saved.

🎉 That's it, your code is ready to be deployed...

## Deployment

1. For this Cloud Challenge, only a function deployed in region `europe-west1` will make you eligible. Make it your default deployment region:
   ```sh
   REGION="europe-west1"
   gcloud config set functions/region $REGION
   ```
2. Deploy your function:
   ```sh
   gcloud functions deploy cloud_challenge_data \
   --source ./src \
   --runtime python310 \
   --trigger-http \
   --allow-unauthenticated
   ```
3. The command output should look like the following:
   ```terminal
   Deploying function (may take a while - up to 2 minutes)...done.
   availableMemoryMb: 256
   entryPoint: cloud_challenge_data
   httpsTrigger:
   url: https://REGION-PROJECT_ID.cloudfunctions.net/cloud_challenge_data
   ...
   ```

🎉 Your function is deployed and can be tested...

## Test

Your function is deployed. Let's test it.

1. Retrieve the URL of your function:
   ```sh
   URL=$(gcloud functions describe cloud_challenge_data --format "value(httpsTrigger.url)")
   echo $URL
   ```
2. This should give you a URL following this format:
   ```terminal
   https://europe-west1-europython22dub-7xxx.cloudfunctions.net/cloud_challenge_data
   ```
3. Call your function:
   ```sh
   curl $URL
   ```
4. You should receive your Cloud Challenge data:
   ```terminal
   {"answer":42,...}
   ```

🎉 Your Cloud Function is functional. You can now register to participate in the raffle...

## Registration

This is now the last step before you're registered for the raffle.

1. Define environment variables for the data and registration endpoints:
   ```sh
   DATA_URL=$(gcloud functions describe cloud_challenge_data --format "value(httpsTrigger.url)")
   REGISTRATION_URL="https://europe-west1-lpdemo-ep22.cloudfunctions.net/cloud_challenge_register"
   ```
2. Call the registration endpoint:
   ```sh
   curl -w "\n" --get $REGISTRATION_URL -d data_url=$DATA_URL
   ```
3. If everything is correct, here is the success message:
   ```terminal
   You're registered!
   ```
4. If you get a different message, this should be self explanatory. You can then fix, redeploy, and retry. If you're stuck, feel free to chat with us at the booth.

🎉 You're now registered to participate in the daily raffles...

## More

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

- Don't forget to come to our booth for the daily raffles.
- Raffles take place during the afternoon break at **15:15**.
- If your name is drawn but you're not there, we'll have to relaunch the wheel.
- Your Google Cloud account is valid during the conference days, benefit from it to complete codelabs on your technologies of interest:
  - https://codelabs.developers.google.com/?category=cloud

And feel free to come to our booth anytime to chat about Google Cloud, Python, or anything.

We wish you the best EuroPython!
