#!/usr/bin/python
import os
import waagentapi

def install(logger, unitpath, unitname):  
    logger.xtnlog("Installing {0} using systemctl".format(unitname))
    # customize the unit with the install location of the extension
    # copy the output of customization to the system folder
    workingdir = os.getcwd()
    waagentapi.RunGetOutPut(logger, "sed #{WORKINGDIR}#{0} {0}/{1} > /lib/systemd/system/{2}".format(workingdir, unitpath, unitname))
    # trigger a scan of the system to get unit loaded
    waagentapi.RunGetOutPut(logger, "systemctl daemon-reload")
    return
    
def uninstall(logger, unitname):
    logger.xtnlog("Uninstalling {0} using systemctl".format(unitname))
    waagentapi.RunGetOutPut("systemctl stop {0} && systemctl disable {0} && rm /lib/systemd/system/{0}".format(unitname))
    return

def update(logger, unitdir, unitname):
    logger.xtnlog("Updating Daemon {0}".format(unitname))
    InstallDaemon(waagentapi, logger, unitdir, unitname)
    return
    
def enable():
    logger.xtnlog("Enabling {0} using systemctl".format(unitname))
    waagentapi.RunGetOutPut("systemctl start {0}".format(unitname))
    return
    
def getStatus():
    logger.xtnlog("Getting {0} status using systemctl".format(unitname))
    status, msg = waagentapi.RunGetOutPut("systemctl is-failed {0}".format(unitname))
    return msg
