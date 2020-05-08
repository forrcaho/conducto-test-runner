
import unittest
import time

class Test014(unittest.TestCase):

    def test_delay(self):
        time.sleep(2.4)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
