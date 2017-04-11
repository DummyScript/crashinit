#!/usr/bin/env python
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
TF_Curses
Alphagriffin.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"

import os, sys
import redis
import numpy as np
import ag.logging as log
log.set(5)

class Database(object):
    def __init__(self):
        self.database = redis.Redis(
            host='agserver')

    def main(self):
        if self.database:
            log.debug("found that database")
            if self.write_data('4', '20'):
                log.debug("wrote that data")
                pass
            twenty = self.read_data('4')
            log.debug("read data test: {}".format(twenty))
            if int(twenty) is 20:
                return True
            log.warn("see here... see.")
            return False
        else:
            log.warn("Not logging into the database.")
        return False

    def check_dataset(self): pass

    def write_data(self, key, value):
        self.database.set(key, value)
        log.debug("write: [{}, {}]".format(key, value))
        return True

    def read_data(self, key):
        value = self.database.get(key).decode('UTF-8')
        log.debug("read: {}, found: {}".format(key, value))
        return value




if __name__ == '__main__':
    log.info("Starting the Database Testing")
    try:
        app = Database()
        if app.main():
           sys.exit("Everything checks out.")
    except Exception as e:
        log.error("and thats okay too.")
        sys.exit(e)