#!/usr/bin/env python3
'''
This acts as base class for writing test scripts.
This creates the required resources to run the test scripts.
Checking commit
Final comment
One more comment
another commenta dded.
change added after two explicit branches
'''
import logging
from restFile import RestBase

## Base class for test scripts.
class TestBase(object):
    def __init__(self):
        self.rest = RestBase()
        self.log = self._getLogging()
        self._results = []

    ## Method to create logger for tests
    def _getLogging(self, level='DEBUG'):
        logger = logging.getLogger(f"{self.__class__.__name__}")
        logLevel = logging.DEBUG if level == 'DEBUG' else logging.INFO
        logger.setLevel(logLevel)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logLevel)
        logFormatter = logging.Formatter("%(name)s:%(asctime)s:%(levelname)s-%(message)s")
        consoleHandler.setFormatter(logFormatter)
        logger.addHandler(consoleHandler)
        return logger

    ## Method to record success of the step
    def recordSuccess(self):
        self._results.append(True)

    ## Method to record failure of the step
    def recordFailure(self):
        self._results.append(False)

    ## Method to publish results at the end of the script
    def publishResults(self):
        print(f"======== Summary of {self.__class__.__name__} ========")
        print(f"Failures  : {self._results.count(False)}")
        print(f"Successes : {self._results.count(True)}")

    ## Setup method to create requites for test script
    def setup(self):
        print(f"Running test {self.__class__.__name__}")

    ## Method to implement verification and validation
    def run(self):
        pass

    ## Method to clean up and revert changes
    def tearDown(self):
        self.publishResults()
