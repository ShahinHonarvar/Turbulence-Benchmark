import re
def palindrome_of_length_n(str):
    str = str.lower()
    return set(re.findall(r'((?=([a-z]))[a-z]{56})', str))
