
import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindrome_set = set()
    
    for i in range(len(s)):
        for j in range(i + 80, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 80 and substring == substring[::-1]:
                if not re.search('[^a-z]', substring):
                    palindrome_set.add(substring)
    return palindrome_set
