import unittest
import calc_tests

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcBasicTests))
calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcExTests))
print(f"Count of tests: {calcTestSuite.countTestCases()} \n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
