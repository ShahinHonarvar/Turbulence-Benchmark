
import re
def palindrome_of_length_n(string):
    n = 53
    result = set()
    string = string.lower()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if re.match('^[a-z]+$', substring):
            if substring == substring[::-1]:
                result.add(substring)
    return result
