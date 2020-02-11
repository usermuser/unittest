"""We can use TestResult class to get information about test results
"""

import unittest
import calc_tests

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(calc_tests)

testResult = unittest.TestResult()    # Error? Do we need this line?

runner = unittest.TextTestRunner(verbosity=2)
testResult = runner.run(suites)

print("errors")
print(len(testResult.errors))
print("failures")
print(len(testResult.failures))
print("skipped")
print(len(testResult.skipped))
print("testsRun")
print(testResult.testsRun)

