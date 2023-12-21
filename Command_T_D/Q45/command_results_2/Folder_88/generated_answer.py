import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?P<palindrome>[a-z]+)[:;.,?]m', s[3:-7:-1]))
