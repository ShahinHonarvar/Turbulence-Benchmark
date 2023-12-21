
import re

def palindromes_of_specific_lengths(string):
    substring = string[24:98]
    palindrome_set = set()
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            palindrome_candidate = substring[i:i+length]
            if re.match(r'^[a-zA-Z]+$', palindrome_candidate) and palindrome_candidate.lower() == palindrome_candidate.lower()[::-1]:
                palindrome_set.add(palindrome_candidate)
    return palindrome_set
