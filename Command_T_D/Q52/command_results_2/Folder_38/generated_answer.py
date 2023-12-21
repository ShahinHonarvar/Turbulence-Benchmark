import re
def palindrome_of_length_n(s):
    return re.findall(r'[a-z]+[a-z]{%38}[a-z]{%38}'.lower(), s)
