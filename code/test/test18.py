
import unittest
import time

class Test018(unittest.TestCase):

    def test_delay(self):
        time.sleep(2.4)
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
