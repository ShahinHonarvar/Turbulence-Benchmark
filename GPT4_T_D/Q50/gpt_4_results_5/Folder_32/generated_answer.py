
from collections import Counter

def if_contains_anagrams(strings_list):
    count = 0
    strings_list = [''.join(sorted(x.lower())) for x in strings_list if len(x)>=3]
    c = Counter(strings_list)
    for val in c.values():
        count += (val*(val-1))//2
    if count >= 194:
        return True
    else:
        return False
