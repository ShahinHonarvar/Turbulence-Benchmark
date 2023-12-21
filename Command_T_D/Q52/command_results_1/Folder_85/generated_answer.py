import re
def palindrome_of_length_n(s):
    return set(re.findall(r'(?i)(?=([^aieou]))([aieou])\1', s))
