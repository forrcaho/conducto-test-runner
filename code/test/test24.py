
import unittest
import time

class Test024(unittest.TestCase):

    def test_delay(self):
        time.sleep(0.9)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
