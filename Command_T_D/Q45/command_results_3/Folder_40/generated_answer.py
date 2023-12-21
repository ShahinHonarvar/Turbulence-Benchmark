import re
def palindromes_between_indices(s):
    str_list = s[4:-5] + s[5:-4] + s[4:-9] + s[9:-4]
    return set(re.findall(r'[a-z]{7,}'.lower(), str_list))
