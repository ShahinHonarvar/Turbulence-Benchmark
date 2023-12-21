import re
def palindromes_between_indices(s):
    reg = re.compile("|".join(c for c in range(ord("a")-1, ord("z")+1) if c in s[6:8]))
    return set(reg.findall(r"(\w)(?=\w\1)"))
