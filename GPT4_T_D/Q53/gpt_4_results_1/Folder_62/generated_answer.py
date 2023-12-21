
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'\W+', '', s).lower()
    palindrome_set = set()
    length_s = len(s)
    for i in range(length_s):
        for j in range(i + 31, length_s + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
