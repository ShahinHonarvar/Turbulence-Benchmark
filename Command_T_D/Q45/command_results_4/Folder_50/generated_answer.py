import re
def palindromes_between_indices(s):
    s = s[4:-8]
    return set(re.findall(r'((?P<i>.{5,})(?P<j>.{1,}))\1(?P<k>.{1,}))\2(?P=i)\3(?P=j)\4(?P=k)', s.lower()))
