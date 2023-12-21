
import re

def palindromes_of_specific_lengths(string):
    substring = string[20:75]
    palindrome_set = set()
    for i in range(len(substring)):
        for j in range(i+36, min(i+43, len(substring)+1)):
            candidate = substring[i:j]
            if candidate.lower() == candidate[::-1].lower() and candidate.isalpha():
                palindrome_set.add(candidate)
    return palindrome_set
