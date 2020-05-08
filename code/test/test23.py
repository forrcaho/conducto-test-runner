
import unittest
import time

class Test023(unittest.TestCase):

    def test_delay(self):
        time.sleep(4.6)
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
