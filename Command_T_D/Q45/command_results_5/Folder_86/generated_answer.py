import re
def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    m = re.fullmatch(r'([a-z]+) ([a-z]+)', s[6:-3])
    if m:
        s1 = m.group(1)
        s2 = m.group(2)
        return set(s1 + s2[::-1] + s2 + s1[::-1])
