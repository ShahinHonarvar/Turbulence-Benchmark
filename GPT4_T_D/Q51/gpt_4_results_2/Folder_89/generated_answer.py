
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(x)) for x in str_list if len(x) >= 3]
    c = Counter(str_list)
    count = sum(v * (v - 1)//2 for v in c.values())
    if count <= 73:
        return True
    else:
        return False
