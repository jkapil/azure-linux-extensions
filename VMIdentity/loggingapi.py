#!/usr/bin/python

class xLogger:
    def __init__(self, hutil):
        self.hutil = hutil
    
    # extension handling log
    def xtnlog(self, message):
        if self.hutil:
            self.hutil.log(str)
        else:
            print(message)
    
    # extension provisoned daemon log
    def syslog(self, level, message):
        if self.hutil:
            self.hutil.syslog(level, message)
        else:
            print("{0} - {1}".format(level, message))
