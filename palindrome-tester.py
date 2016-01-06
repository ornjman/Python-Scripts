#!/usr/bin/env python

# -- About ---------------------------------------------------------------------------
# 
# This script is designed to test a string for being a palindrome at the command line.
#
#  - The program works by iterating through each letter of the string from the beginning
#    and then comparing it to the next letter in the reverse direction.
#
#  - The string can contain new lines, punctuation and capitalization
#    that are not counted against the string being a palindrome
#
# -- Usage ----------------------------------------------------------------------------
# 
# At the command-line provide the string as the first argument, for example:
# 
#	python palindrome-tester.py "Am I a palindrome?"
# 	
# 
# -- Missing functionality ------------------------------------------------------------
# STDIN as input for a string

# import the sys library for capturing passed arguments
import sys

# define the function with string parameter
def is_palindrome(s):

	# establish reversed character index
	reverse_character_index = len(s) - 1

	# iterate through each letter, starting from the beginning
	for i, c in enumerate(s):

		# capture the middle point
		middle_point = len(s)/2 - 1;

		# check index is not greater than or equal to the middle point, 
		# which is the floor of half the letter count
		if i <= middle_point:

			# check the forward running index is an alpha character
			if not c.isalpha():
				
				# move to next character since current invalid
				continue;

			# find the next alphabetic letter or stop when you reach the middle point
			while not s[reverse_character_index].isalpha():

				# ensure the reverse character index has not passed the middle point
				if reverse_character_index > middle_point:

					# move to the next character 
					reverse_character_index -= 1

				# reverse index has passed the middle point
				else:
					# return failure status
					return False

			# check that the current character matches the next character in reverse
			if c.lower() == s[reverse_character_index].lower():

				# increase the reverse index count
				reverse_character_index -= 1

			# characters do not match
			else:
				# return failure status
				return False
			
		# successful on making it to the center point
		else:
			# return success status
			return True

# check for passed arguments
if len(sys.argv) > 1:

	# automatically test and execute for the only passed argument
	if is_palindrome(sys.argv[1]):
		
		# print palindrome status
		print "Palindrome"

	# not a palindrome
	else:
		# print non-palindrome status
		print "Not a palindrome"
else:
	# notify of missing parameters
	print "Error: Please provide a string to test"
