import unittest
import calc


class CalcTest(unittest.TestCase):
    """Calc Tests"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up for class"""
        print("SetUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down for class"""
        print("=============")
        print("TearDownClass")

    def setUp(self) -> None:
        """Set up for test"""
        print(f"Set up for '[ {self.shortDescription()} ]' ")

    def tearDown(self) -> None:
        """Tear down down for test"""
        print(f"Tear for '[ {self.shortDescription()} ]' \n")

    def test_add(self):
        """Add operation test"""
        print(f'id: {self.id()}')
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        """Sub operation test"""
        print(f'id: {self.id()}')
        self.assertEqual(calc.sub(4, 2), 2)

    def test_mul(self):
        """Mul operation test"""
        print(f'id: {self.id()}')
        self.assertEqual(calc.mul(2, 5), 10)

    def test_div(self):
        """Div operation test"""
        print(f'id: {self.id()}')
        self.assertEqual(calc.div(8, 4), 2)


if __name__ == '__main__':
    unittest.main()
