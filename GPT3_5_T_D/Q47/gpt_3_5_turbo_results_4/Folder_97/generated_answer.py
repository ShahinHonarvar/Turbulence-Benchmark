
import re

def palindromes_of_specific_lengths(string):
    substring = string[28:95].lower()
    pattern = re.compile(r'[a-zA-Z]{38,49}')
    palindromes = set(re.findall(pattern, substring))
    return {palindrome for palindrome in palindromes if palindrome == palindrome[::-1]}
