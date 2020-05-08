
import unittest
import time

class Test021(unittest.TestCase):

    def test_delay(self):
        time.sleep(2.8)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
