import re
def palindromes_between_indices(s):
    return re.findall(r"((?i)(?<=\A)[a-z]){3}(?=([A-Z][a-z]*\Z)|$)", s)
