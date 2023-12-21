import re
def palindrome_of_length_at_least_n(test_str):
    # find all palindromes
    # use a regular expression to match all palindromes
    # use the flag I to ignore the case
    pal_str = re.findall(r'[a-z]{50}', test_str.lower(), flags=re.I)
    # return the set of all palindromes
    return set(pal_str)
