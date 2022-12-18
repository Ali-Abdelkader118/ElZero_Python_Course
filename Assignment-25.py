# Test 1 => 10 Is Found In This List [5, 7, 8, 10]
# Test 2 => The Type Of 10 Is Int
# Test 3 => Number 100 Return True
# Test 4 => Empty List [] Return False
# Test 5 => 100 Is Larger Than Or Equal 90

import unittest
import string
import random

# Assignment-1


class MyTestCases(unittest.TestCase):

    def test_one(self):
        self.assertIn(10, [5, 7, 8, 10], "Should Be True")
        print("Test 1 => 10 Is Found In This List [5, 7, 8, 10]")

    def test_two(self):
        self.assertIsInstance(10, int, "Should Be True")
        print("Test 2 => The Type Of 10 Is Int")

    def test_three(self):
        self.assertTrue(100, "Should Be True")
        print("Test 3 => Number 100 Return True")

    def test_four(self):
        self.assertFalse([], "Should Be False")
        print("Test 4 => Empty List [] Return False")

    def test_five(self):
        self.assertGreaterEqual(100, 90, "Should Be True")
        print("Test 5 => 100 Is Larger Than Or Equal 90")


# Assignment-2


def make_serial():

    num = 14

    all_char = string.ascii_letters + string.digits
    char_num = len(all_char)
    serial_list = []

    while num > 0:
        random_num = random.randint(0, char_num - 1)

        random_char = all_char[random_num]

        serial_list.append(random_char)

        num -= 1

    part1 = "".join(serial_list)[0:4]
    part2 = "".join(serial_list)[4:8]
    part3 = "".join(serial_list)[8:14]
    serial = (part1, part2, part3)
    final_serial = "-".join(serial)

    print(final_serial)


make_serial()

if __name__ == "__main__":
    unittest.main()
