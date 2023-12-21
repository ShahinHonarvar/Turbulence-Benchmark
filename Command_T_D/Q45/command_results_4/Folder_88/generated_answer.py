import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?=([^aieouAEIOU]{%d}))([aieouAEIOU]{%d}[aieouAEIOU]{%d})([aieouAEIOU]{%d}[aieouAEIOU]{%d})' % (4, 4, 4, 4, 4, 4), s))
