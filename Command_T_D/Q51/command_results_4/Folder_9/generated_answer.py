import re
def if_contains_anagrams(s):
    return len(set(a for s1 in s for s2 in s for a in zip(s1, s2))) <= 475
