
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i+133, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
