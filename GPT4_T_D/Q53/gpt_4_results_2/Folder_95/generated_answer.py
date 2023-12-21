
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'[^A-Za-z]', "", s).lower()
    result = set()
    for i in range(35, len(s) + 1):
        for j in range(len(s) - i + 1):
            temp = s[j: j + i]
            if temp == temp[::-1]:
                result.add(temp)
    return result
