
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-z]+', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+82, len(s)):
            substr = s[i:j+1]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
