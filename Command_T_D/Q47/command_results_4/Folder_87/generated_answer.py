import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=.*[a-z]){11}(?P<palindrome>[a-z]{34,54}[a-z]{34,54}[a-z]{11})', s))
