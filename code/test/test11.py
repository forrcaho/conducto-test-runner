
import unittest
import time

class Test011(unittest.TestCase):

    def test_delay(self):
        time.sleep(1.9)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
