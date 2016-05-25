# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from flask import Flask
import string
import random

import logging
from gcloud import storage
from subprocess import call

import os 

app = Flask(__name__)
app.config['SECRET_KEY']='test'

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/transcode')
def transcode():
    client = storage.Client('appengine-transcoder')
    bucket = client.bucket('appengine-transcoder')
    blob = bucket.blob('sample2.mp4')
    f = open('/tmp/sample2.mp4', 'w')
    blob.download_to_file(f)
    ret = os.system('/usr/bin/avconv -i /tmp/sample2.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis /tmp/output.webm')
    if ret:
        return "Failed"
    blob = bucket.blob('output.webm')
    blob.upload_from_file('/tmp/output.webm')
    return "Done"


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
