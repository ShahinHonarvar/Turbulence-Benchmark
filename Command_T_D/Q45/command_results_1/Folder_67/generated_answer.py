import re
def palindromes_between_indices(str1):
    str1 = str1.lower()
    pat = re.compile(r'[a-z]{%d}{%d}{%d}{%d}{%d}{%d}' % (2, 3, 4, 5, 6))
    return set(re.match(pat, s).group() for s in str1[::-1])
