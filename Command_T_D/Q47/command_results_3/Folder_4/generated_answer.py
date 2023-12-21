import re
def palindromes_of_specific_lengths(str):
    str = str.lower()
    return set(re.findall(r"<(palindrome){17,66}>([a-z]){12,92}(</palindrome>)", str))
