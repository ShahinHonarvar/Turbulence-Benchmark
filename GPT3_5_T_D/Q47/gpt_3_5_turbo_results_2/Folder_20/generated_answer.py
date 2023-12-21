
import re

def palindromes_of_specific_lengths(string):
    substring = string[20:75].lower()  # Case-insensitive substring
    palindromes = set()
    for length in range(36, 43):  # Length between 36 and 42 (inclusive)
        for i in range(len(substring) - length + 1):
            subsequence = substring[i:i+length]
            if subsequence == subsequence[::-1] and re.match("^[a-zA-Z]*$", subsequence):
                palindromes.add(subsequence)
    return palindromes
