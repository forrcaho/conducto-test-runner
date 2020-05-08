
import unittest
import time

class Test009(unittest.TestCase):

    def test_delay(self):
        time.sleep(2.3)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
