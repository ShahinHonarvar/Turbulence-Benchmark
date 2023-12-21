import re
def palindromes_between_indices(s):
    if not s:
        return set()
    i = s.lower().count("e") + s.lower().count("i") + s.lower().count("o")
    if i >= 2:
        return set(re.findall(r'[eio]?.+[ioe]', s[2:-2]))
    else:
        return set()
