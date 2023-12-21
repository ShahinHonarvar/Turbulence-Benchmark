import re
def palindromes_between_indices(s):
    m = re.findall(r'(?P<A>.{8})(?P<B>.{8})(?P=A)', s.lower())
    return set(m)
