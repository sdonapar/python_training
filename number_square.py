import unittest

def number_square(n):
    if n == 0:
        return 0
    elif (n > 0):
        return n**2
    else:
        return -1

class test_number_square(unittest.TestCase):
    
    def test_zero_input(self):
        self.assertEqual(number_square(0),0)
    def test_positive_input(self):
        self.assertEqual(number_square(5),25)
    def test_invalid_input(self):
        self.assertEqual(number_square(-6),-1)

if __name__ == '__main__':
	unittest.main()