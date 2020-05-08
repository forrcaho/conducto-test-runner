
import unittest
import time

class Test022(unittest.TestCase):

    def test_delay(self):
        time.sleep(3.1)
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
