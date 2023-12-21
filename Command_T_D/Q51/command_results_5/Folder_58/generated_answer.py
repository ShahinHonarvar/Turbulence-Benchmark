import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([A-Z])\1+)(?=\D\1+)(?=\D[A-Z]\1+)', s))
