
import re

def palindromes_of_specific_lengths(input_string):
    substring = input_string[18:99].lower()
    palindromes = set()

    for length in range(31, 52):
        for start in range(0, len(substring) - length + 1):
            potential_palindrome = substring[start: start + length]
            
            if re.match('^[a-z]*$', potential_palindrome) and potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)

    return palindromes
