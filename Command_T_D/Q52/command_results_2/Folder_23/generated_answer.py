import re
def palindrome_of_length_n(s):
    if len(s) < 69:
        return set()
    return set(re.findall(r'(?i)(?:[a-z]+){66}(?:[a-z]+){1,2}', s))
