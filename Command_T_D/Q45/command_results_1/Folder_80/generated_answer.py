import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?=([a-z]))(a)(b)(c)(d)(e)(f)(g)(h)', s[3:-8:]))
