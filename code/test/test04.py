
import unittest
import time

class Test004(unittest.TestCase):

    def test_delay(self):
        time.sleep(1.3)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
