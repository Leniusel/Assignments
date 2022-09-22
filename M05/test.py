#Doris Tran
#September 21, 2022
#M05 Assignment - Testing

#Writing your first test
import unittest
#from my_sum import sum

#import fractions
from fractions import Fraction

#Writing your first Test: Testing a list of integers
class TestSum(unittest.TestCase):

#Testing your code (unittest portion) - using a test runner
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6") 
        #Will be true, so no error produced on this line

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6") 
#After running the code, test_sum_tuple will fail: it states 5 != 6. Using nose2 from the command prompt give the same results.   


#Writing your first Test: Testing a list of integers
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6) #check if result is equal to 6
        #After running, the test will come as true and nothing is printed for test_list_int

    #Test fractions
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
        #After running, there will be an assert error since the sum does not equal 1.

#Excecute=ing your first test
if __name__ == '__main__':
    unittest.main()
 #This piece of code tells the program to excecute the test runner   

 #Overall, there's a total of 4 tests, 2 of which failed due to assertion error as stated in the tutorial.
