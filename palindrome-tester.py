#!/usr/bin/env python

# This is designed to test a string for being a palindrome.

# import the sys library for capturing passed arguments
import sys

# define the function with string parameter
def is_palindrome(s):

	# establish reversed character index
	reverse_character_index = len(s) - 1

	# iterate through each letter, starting from the beginning
	for i, c in enumerate(s):

		# check index is not greater than the floor of half the letter count
		if i <= len(s)/2 - 1:

			# check for valid characters
			if not c.isalpha():
				
				# move to next character since current invalid
				continue;

			# find the next alphabetic letter
			while not s[reverse_character_index].isalpha():

				# increase the reverse index count
				reverse_character_index -= 1

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

if len(sys.argv) > 1:
	# automatically execute for the only passed argument
	print is_palindrome(sys.argv[1])
else:
	print "Error: Please provide a string to test"
