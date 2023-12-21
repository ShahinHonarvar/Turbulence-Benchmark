import re
def if_contains_anagrams(s):
    return not (s and len(s)>=3 and all(x.lower() in y.lower() for x,y in zip(s,s)))
