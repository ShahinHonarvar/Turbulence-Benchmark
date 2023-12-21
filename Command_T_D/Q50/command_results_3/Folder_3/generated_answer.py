import re
def if_contains_anagrams(list):
    return bool(re.findall(r'\A[a-z]{3}([a-z]{%d}\1){2}\Z' % (len(list), list), list))
