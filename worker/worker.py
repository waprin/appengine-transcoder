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

import os
from gcloud import storage, pubsub
import psq
import sys

TOPIC = 'projects/adept-button-132222/topics/message'
PROJECT_ID = 'adept-button-132222'

def transcode():
    client = storage.Client(PROJECT_ID)
    bucket = client.bucket('appengine-transcoder')
    blob = bucket.blob('sample.mp4')
    with open('/tmp/sample2.mp4', 'w') as f:
        blob.download_to_file(f)
    os.system('rm /tmp/output.webm')
    ret = os.system('/usr/bin/avconv -i /tmp/sample2.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis /tmp/output.webm')
    if ret:
        sys.stderr.write("FAILED")
        return "Failed"
    blob = bucket.blob('output.webm')
    blob.upload_from_file(open('/tmp/output.webm'))
    sys.stderr.write("SUCCESS")
    return "SUCCESS"

if __name__ == '__main__':
    pubsub_client = pubsub.Client(PROJECT_ID)
    topic = pubsub_client.topic("message")
    sub = pubsub.Subscription("mysub", topic=topic)
    sys.stderr.write("Polling the topic")
    while True:
        messages = sub.pull(
            return_immediately=False, max_messages=110)
        if messages:
            transcode()




