#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import requests
import json
import pprint

# Update to match your API key
API_KEY = '#'

# Update to match your chosen parameters
SINCE = ''
UNTIL = ''
DATE_RANGE = ''
STATUSES = []
INCIDENT_KEY = ''
SERVICE_IDS = []
TEAM_IDS = []
USER_IDS = []
URGENCIES = []
TIME_ZONE = 'UTC'
SORT_BY = []
INCLUDE = []

def list_incidents():
    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token=' + API_KEY
    }
    payload = {
        'since': SINCE,
        'until': UNTIL,
        'date_range': DATE_RANGE,
        'statuses': STATUSES,
        'incident_key': INCIDENT_KEY,
        'service_ids': SERVICE_IDS,
        'team_ids': TEAM_IDS,
        'user_ids': USER_IDS,
        'urgencies': URGENCIES,
        'time_zone': TIME_ZONE,
        'sort_by': SORT_BY,
        'include': INCLUDE
    }
    r = requests.get(url, headers=headers, params=json.dumps(payload))
    pprint.pprint('Status Code: ' + str(r.status_code))
    pprint.pprint(r.json())

if __name__ == '__main__':
    list_incidents()