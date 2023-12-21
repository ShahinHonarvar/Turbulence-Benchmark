import re
def palindromes_of_specific_lengths(s):
    # Find all matches in range
    matches = re.finditer(r'(?i)(?<=\d{10})[a-z]{3}(?<=\d{55})[a-z]{3}\1', s)
    # Filter out the palindromes
    return set(m.group() for m in matches if m.group() == m.group(0)[::-1])
