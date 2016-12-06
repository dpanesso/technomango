# -*- coding: utf-8 -*-
#
# For use with TP-Link HS-100 or HS-110
#  
# by David Panesso
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
#
import os
import json

import schedule
import time
import utils

version = 0.1

DEBUG = False

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


def check_info():

    data = utils.send_cmd('info')
    if DEBUG:
        print "Sent:     ", utils.commands['info']
        print "Received: ", json.dumps(json.loads(data), indent=4)
    filename = os.path.join(SITE_ROOT, "static/", 'data.json')
    with open(filename, 'w') as outfile:
        json.dump(json.loads(data), outfile, indent=4)

schedule.every(5).seconds.do(check_info)

while 1:
    schedule.run_pending()
    time.sleep(1)
