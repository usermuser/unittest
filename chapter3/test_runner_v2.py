"""In this version of our test runner we use
loadTestsFromModule method to load all tests from module calc_tests

loadTestsFromModule(module, pattern=None)
"""

import unittest
import calc_tests

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(calc_tests)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suites)
