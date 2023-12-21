import re
def palindromes_of_specific_lengths(s):
    # Code to find palindromes
    # Only 5 to 10 characters long
    # Located in the range of 100 to 200
    # Only letters
    # Case insensitive
    return set(re.findall(r'(?i)(?=.*[a-z]){5,10}(?=.*[a-z]{100,200})', s))
