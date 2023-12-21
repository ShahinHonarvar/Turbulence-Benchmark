import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'[a-z]{1,17}(?i)(?=([a-z]{1,66}(?i)[a-z]{1,17}){0,92})[a-z]{1,66}(?i)[a-z]{1,17})', s)}
