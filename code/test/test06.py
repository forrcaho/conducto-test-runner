
import unittest
import time

class Test006(unittest.TestCase):

    def test_delay(self):
        time.sleep(4.5)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
