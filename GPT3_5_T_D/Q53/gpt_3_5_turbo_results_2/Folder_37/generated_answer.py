
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i+67, len(string)+1):
            palindrome_candidate = string[i:j]
            if re.match("^[a-zA-Z]+$", palindrome_candidate) and palindrome_candidate == palindrome_candidate[::-1]:
                palindromes.add(palindrome_candidate)
    return palindromes
