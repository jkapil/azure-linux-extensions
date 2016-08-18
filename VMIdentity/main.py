#!/usr/bin/env python
#
# VMIdentity extension
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

from Utils.WAAgentUtil import wagent
import Utils.HandlerUtil as Util

import constants.py
from logginapi import xtnLogger



def install():
    hutil, xLogger = waagentapi.initialize()
    xLogger.xlog("Installation Started...")

    hutil.do_parse_context("Install")
    systemd.install(xLogger, Constants.SystemdUnitPath, Constants.SystemdUnitName)
    hutil.do_exit(0, "Install", "Success", '0', "Installation Succeeded")


def uninstall():
    hutil, xLogger = waagentapi.initialize()
    hutil.xlog("UnInstall Started...")

    hutil.do_parse_context("UnInstall")
    systemd.unistall(xLogger, Constants.SystemdUnitName)
    hutil.do_exit(0, "UnInstall", "Success", '0', "UnInstall Succeeded")


def update():
    hutil, xLogger = waagentapi.initialize()
    xLogger.xlog("Update Started...")

    hutil.do_parse_context("Update")
    hutil.do_exit(0, "Update", "Success", '0', "Update Succeeded")

def main():
    try:
        for a in sys.argv[1:]:
            if re.match("^([-/]*)(disable)", a):
                disable()
            elif re.match("^([-/]*)(uninstall)", a):
                uninstall()
            elif re.match("^([-/]*)(install)", a):
                install()
            elif re.match("^([-/]*)(enable)", a):
                enable()
            elif re.match("^([-/]*)(update)", a):
                update()
    except Exception as e:
        err_msg = "Failed with error: {0}, {1}".format(e, traceback.format_exc())
        waagent.Error(err_msg)

if __name__ == '__main__' :
    main()
