########################################################################################################################
# Class: Computer Networks
# Date: 02/03/2020
# Lab0: Getting Started with Python
# Goal: Learning the basics of Python
# Student Name:
# Student ID:
# Student Github Username:
# Instructions: Complete the TODO sections for each problem
# Guidelines: Read each problem carefully, and implement them correctly. Grade is based on lab correctness/completeness
#               No partial credit will be given.
#               No unit test are provided for lab #0
########################################################################################################################

########################## Problem 0: Print  ###########################################################################
"""
Print your name, student id and Github username
Sample output:
Name: Jose
SID: 91744100
Github Username:
"""
import unittest

name = ""  # TODO: your name
SID = 000000000  # TODO: your student id
git_username = ""  # TODO: your github username
print(name)
print(SID)
print(git_username)
print('\n')

########################## Problem 1: product or sum ############################################################
"""
Given two values representing two integers, return their product if it is less or equal than the threshold, 
Otherwise, return their sum. 
Example with product: value1 = 2, value2 = 3, threshold = 100 will return 6
Example with sum: value1 = 2, value2 = 100, threshold = 100 will return 102
"""


def product_or_sum(value1, value2, threshold=100):
    """
    :value1: an integer representing the first value
    :value2: an integer representing the second value
    :threshold: an integer representing the limit for the product of the two values
    :return: the product or the sum of both values
    """
    result = 0
    # TODO: your code here
    return result


########################## Problem 2: String Processing ##############################################################
"""
Given a string print the number of times the another string appears anywhere in the given string

For example, given the string: "Alice and Bob go to the same school. They learned today in class how to treat a lice 
infestation, and Alice found the lecture really interesting". the string "Alice" will be found 2 times. 
"""


def str_times_found(str_to_find, original_str):
    """
    :str_to_find: the string to be found
    :original_str: the string where str_to_find may be found.
    :return: an integer representing the number of times str_to_find was found
    """
    result = 0
    # TODO: your code here
    return result


########################## Problem 3: Loops ############################################################################
"""
Given a list of numbers iterate over them and output the sum of the current number and previous one.

Given: [5, 10, 24, 32, 88, 90, 100], returns [5, 15, 34, 56, 120, 178, 190]
"""


def summation(list_of_integers):
    """
    :list_of_integers: represents the given list of integers
    :returns: a new list where the value in index (i) is the sum of list_of_integers[i-1] + list_of_integers[i]
    """
    result = []
    # TODO: your code here
    return result


########################## Problem 4: Merging Lists ##########################################################
"""
Given two unordered lists as parameters, return a new list with all the 
odd numbers from the first and second list sorted in ascending order. 

For example: Given l1 = [2,1,5,7,9] and l2 = [32,33,13] the function will return odds = [1,5,7,9,13,33] 
"""


def merge_odds(list1, list2):
    """
    :list1:
    :list2:
    :return: a new ordered list with all the odds values from both lists.
    """
    odds = []
    # TODO: your code here
    return odds


########################## Problem 5: Dictionaries ###################################################
"""
Refactor problem #4 to return a python dictionary instead of a list where the keys are the indexes of the odd numbers 
(from list1 and list2) and the values are the odd numbers. 

For example: Given [2,1,5,7,9] and [32,33,13] the function returns {1: [1, 33], 2: [5,13], 3: [7], 4: [9]} 
"""


def merge_odds_with_keys(list1, list2):
    """
    :list1:
    :list2:
    :return: a Python dictionary of keys (indexes in list1 and list2), and values are the odd values.
    """
    odds = {}
    # TODO: your code here
    return odds


######################## Unit Tests (Do not modify) ##################################################################

class TestCases(unittest.TestCase):
    def testP1(self):
        self.assertEqual(product_or_sum(2, 5), 10)
        self.assertNotEqual(product_or_sum(2, 5, threshold=9), 10)

    def testP2(self):
        str = "Alice and Bob go to the same school. They learned today in class how to treat a lice" \
              "infestation, and Alice found the lecture really interesting"
        self.assertEqual(str_times_found("Alice", str), 2)

    def testP3(self):
        list_of_values = [5, 10, 24, 32, 88, 90, 100]
        self.assertEqual(summation(list_of_values), [5, 15, 34, 56, 120, 178, 190])

    def testP4(self):
        list1 = [2, 1, 5, 7, 9]
        list2 = [32, 33, 13]
        odds = merge_odds(list1, list2)
        self.assertEqual(odds, [1, 5, 7, 9, 13, 33])

    def testP5(self):
        list1 = [2, 1, 5, 7, 9]
        list2 = [32, 33, 13]
        odds = merge_odds_with_keys(list1, list2)
        self.assertEqual(odds, {1: [1, 33], 2: [5, 13], 3: [7], 4: [9]})


if __name__ == '__main__':
    unittest.main()
