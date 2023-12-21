import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'(?i)(?P<palindrome>[a-z]{50,51})(?P<nonpalindrome>[a-z]{0,17})(?P<palindrome>[a-z]{0,72})', s)
