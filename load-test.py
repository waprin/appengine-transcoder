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

# A simple load test to demonstrate autoscaling

import time
import requests

PROJECT_ID = 'your-project-id'
URL = 'https://{}.appspot.com/transcode'.format(PROJECT_ID)
NUM_REQUESTS = 100
DELAY=.1

for i in range(0, NUM_REQUESTS):
    requests.get(URL)
    time.sleep(DELAY)
