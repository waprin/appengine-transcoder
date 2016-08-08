# AppEngine Transcoder Example

Demonstration of using libav in App Engine Flexible Environment.

Please note this is a simple demonstration repo and not ready to productionize!

See the associated Medium post for more info. Please use the Issue Tracker for any problems.

## Overview

Docekrfile and  app.yaml are used to configure the main web worker, main.py.

worker/ contains the Dockerfile and code for the background process that does the transcoding.

## Deploying

Create a Google Cloud project. Download the Google Cloud SDK.

    gcloud init <your-project-id>

go in to the worker/ directory and replace PROJECT_ID with your project ID, then

    gcloud app deploy worker.yaml

That will deploy the backend module. To deploy the frontend module, replace PROJECT_ID
in main.py with your project ID. Then

    gcloud app deploy app.yaml

After that, hitting https://<your-project-id>.appspot.com/transcode will kick off the transcoding
process.

## Help

File and issue on the issue tracker.

## Contributing changes

* See [CONTRIBUTING.md](CONTRIBUTING.md)

## Licensing

* See [LICENSE](LICENSE)
