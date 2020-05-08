
import unittest
import time

class Test010(unittest.TestCase):

    def test_delay(self):
        time.sleep(1.5)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
