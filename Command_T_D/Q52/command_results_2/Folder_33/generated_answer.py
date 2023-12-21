import re
def palindrome_of_length_n(s):
    return re.findall(r'(?i)(?=.)(.)\1(?!\1).{475}(?!\1).{475}(?!\1)', s)
