import re
def if_contains_anagrams(s):
    return not (len(s)>=3 and (set(s) - set("abcdefghijklmnopqrstuvwxyz")).intersection(s))
