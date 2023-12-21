import re
def palindromes_between_indices(s):
    return set(re.findall(r"((?=([^aieou])\1)[^aieou]*((?<=\1)[^aieou])\2\2)", s[4:-7]))
