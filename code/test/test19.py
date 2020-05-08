
import unittest
import time

class Test019(unittest.TestCase):

    def test_delay(self):
        time.sleep(0.5)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
