
import unittest
import time

class Test008(unittest.TestCase):

    def test_delay(self):
        time.sleep(1.8)
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
