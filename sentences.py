"""
This module contains functions that will return the mean, sum,
or median of a list of numbers as a complete sentence.
"""

from statistics import mean
from statistics import median

def printMean(a_list):
	'''Returns the mean of a list, rounded to the hundredths, in a complete sentence.'''
	m = mean(a_list)
	return f"The mean of the numbers provided is {round(m, 2)}."
	
def printSum(a_list):
	'''Returns the sum of a list in a complete sentence.'''
	s = sum(a_list)
	return f"The sum of the numbers provided is {s}."
	
def printMedian(a_list):
	'''Returns the median of a list in a complete sentence.'''
	m = median(a_list)
	return f"The median of the numbers provided is {m}."

if __name__ == "__main__":
	main()