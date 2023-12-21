import re
def if_contains_anagrams(strs):
    return (sum(map(lambda x: bool(re.search(r"((?i)[a-z]){3}[0-9])".format(x), strs)) <= 276)
