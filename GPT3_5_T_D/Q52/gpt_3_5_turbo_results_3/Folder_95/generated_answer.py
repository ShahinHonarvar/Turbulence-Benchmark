
import re

def palindrome_of_length_n(string):
    palindrome_set = set()
    normalized_string = re.sub(r'[^a-zA-Z]', '', string.lower())
    
    for i in range(len(normalized_string)-86):
        palindromic_substring = normalized_string[i: i+87]
        if palindromic_substring == palindromic_substring[::-1]:
            palindrome_set.add(palindromic_substring)
    
    return palindrome_set
