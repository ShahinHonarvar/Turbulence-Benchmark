import re
def palindromes_of_specific_lengths(s):
    # Your code here.
    return re.findall(r'[a-z]+\d{13}([a-z]+){42}([a-z]+\d{13})', s[44:-4], flags=re.I)
