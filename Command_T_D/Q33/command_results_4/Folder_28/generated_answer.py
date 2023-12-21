import re
def return_vowels(s):
    m = re.match(r'[A-Z][^W][.EIOU]{%d,%d}' % (41, 50), s)
    return [i for i in range(m.end() - 1, m.start() - 1, -1) if s[i].isalpha() and s[i] in 'AEIOU']
