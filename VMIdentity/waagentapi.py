#!/usr/bin/python
from Utils.WAAgentUtil import waagent
from loggingapi import xtnLogger

def initialize():
    waagent.LoggerInit('/var/log/waagent.log', '/dev/stdout')
    waagent.Log("%s started to handle.", %(Constants.ExtensionShortName))
    hutil = Util.HandlerUtility(waagent.Log, waagent.Error)
    xLogger = xLogger(hutil)
    return hutil, xLogger

def RunGetOutPut(logger, cmd):
    logger.Print("RunCmd "+cmd)
    error, msg = waagent.RunGetOutput(cmd, chk_err=True)
    logger.xtnlog("Return "+str(error)+":"+msg)
    return error, msg

