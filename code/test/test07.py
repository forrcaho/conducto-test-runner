
import unittest
import time

class Test007(unittest.TestCase):

    def test_delay(self):
        time.sleep(3.2)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
