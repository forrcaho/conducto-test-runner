
import unittest
import time

class Test002(unittest.TestCase):

    def test_delay(self):
        time.sleep(1.2)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
