
import re

def palindromes_of_specific_lengths(string):
    substr = string[30:85]
    palindrome_set = set()
    for length in range(12, 21):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i+length]
            normalized_substring = re.sub('[^a-zA-Z]', '', substring.lower())
            if normalized_substring == normalized_substring[::-1]:
                palindrome_set.add(normalized_substring)
    return palindrome_set
