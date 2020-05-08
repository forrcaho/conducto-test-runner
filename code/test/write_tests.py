import random

test_contents = """
import unittest
import time

class Test{:03d}(unittest.TestCase):

    def test_delay(self):
        time.sleep({})
        self.assertTrue({})

if __name__ == "__main__":
    unittest.main()
"""


for num in range(1, 26):
    sleep_time = "{:0.1f}".format(random.randint(5, 50)/10)
    success = True
    if random.randint(1,10) <= 1: success = False
    fname = f"test{num:02}.py"
    with open(fname, 'w') as f:
        f.write(test_contents.format(num, sleep_time, success))
