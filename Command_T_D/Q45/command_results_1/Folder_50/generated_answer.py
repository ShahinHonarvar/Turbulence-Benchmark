import re
def palindromes_between_indices(str):
    return set(re.findall(r'(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[A-Z])\1\2\3\4\5\6\7\8\1\2\3\4\5\6\7\8', str.lower()))
