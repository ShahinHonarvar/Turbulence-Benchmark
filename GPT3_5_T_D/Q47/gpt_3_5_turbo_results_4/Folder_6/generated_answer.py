
import re

def palindromes_of_specific_lengths(string):
    substring = string[45:99]
    substring = re.sub("[^a-zA-Z]", "", substring)
    substring = substring.lower()

    palindrome_set = set()
    for length in range(40, 48):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1]:
                palindrome_set.add(sub)
    
    return palindrome_set
