#!/usr/bin/env python
#
# VM Identity Refresh Service Provisioned by VM Identity Extension
#
# Copyright 2014 Microsoft Corporation
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
import sys
import re
import time
import logging
from loggingapi import xLogger

def daemon(logger):
    while True:
        work(logger)
        time.sleep(10)

def work(logger):
    logger.syslog(logging.INFO, "I am running {0}".format(time.ctime()))


def main():
    logger = xLogger(None)
    try:
        for a in sys.argv[1:]:
            if re.match("^([-/]*)(work)", a):
                work(logger)                
            elif re.match("^([-/]*)(daemon)", a):
                daemon(logger)
    except Exception as e:
        err_msg = "Failed with error: {0}, {1}".format(e, traceback.format_exc())

if __name__ == '__main__' :
    main()
