import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r"(?i)([a-z]{20})([a-z]{5})([a-z]{20})", text[15:95]))
