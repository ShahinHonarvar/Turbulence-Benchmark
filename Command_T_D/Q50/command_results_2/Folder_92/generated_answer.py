import re
def if_contains_anagrams(strs):
    return bool(re.findall(r"(?=([a-z]{3,})[a-z]{3,}([a-z]{%d,})[a-z]{%d,})[a-z]{%d,})".format(3, 3, 3), strs))
