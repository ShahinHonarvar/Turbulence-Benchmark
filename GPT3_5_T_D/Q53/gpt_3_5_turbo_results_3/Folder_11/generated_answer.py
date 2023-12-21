
import re

def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(54, len(s) - i + 1):
            substring = s[i:i+j]
            if re.match(r'^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
