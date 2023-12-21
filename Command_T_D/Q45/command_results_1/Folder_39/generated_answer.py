import re
def palindromes_between_indices(s):
    s = re.sub(r'([A-Z])', r' \1', s)
    return set(re.findall(r'(.)\1\2\3\4\5', s))
