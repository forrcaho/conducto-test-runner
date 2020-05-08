
import unittest
import time

class Test013(unittest.TestCase):

    def test_delay(self):
        time.sleep(0.8)
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
