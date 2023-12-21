import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?<=.)[a-z]{(136..151)}[a-z]{%(length)i}(?=.)' % {'length': 136, 'string': s[106:280]})}
