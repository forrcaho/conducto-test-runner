
import unittest
import time

class Test020(unittest.TestCase):

    def test_delay(self):
        time.sleep(4.6)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
