import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'((?=.)[a-z]){103,}([a-z]'.format(len=153), s, flags=re.I)}
