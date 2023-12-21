
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 52, length):
            substring = s[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
