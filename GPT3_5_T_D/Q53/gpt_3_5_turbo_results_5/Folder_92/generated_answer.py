
import re

def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)-9):
        for j in range(i+10, len(s)+1):
            temp = s[i:j]
            if temp == temp[::-1] and re.match("^[a-zA-Z]+$", temp):
                result.add(temp)
    return result
