
import unittest
import time

class Test015(unittest.TestCase):

    def test_delay(self):
        time.sleep(1.4)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
