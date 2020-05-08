
import unittest
import time

class Test017(unittest.TestCase):

    def test_delay(self):
        time.sleep(4.1)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
