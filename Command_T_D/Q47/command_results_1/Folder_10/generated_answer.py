import re
def palindromes_of_specific_lengths(test_str):
    return {m.group() for m in re.finditer(r'[a-z]{16,39}(?=\W|$)', test_str[16:60], flags=re.I)}
