"""In this example, only tests from class CalcBasicTests,
for this we use loadTestsFromName method
"""

import unittest
import calc_tests

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromName("calc_tests.CalcBasicTests")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suites)
