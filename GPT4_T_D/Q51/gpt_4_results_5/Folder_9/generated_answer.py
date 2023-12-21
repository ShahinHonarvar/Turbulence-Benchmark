
from collections import Counter

def if_contains_anagrams(string_list):
    string_list = [s.lower() for s in string_list if len(s) >= 3]
    c = Counter([''.join(sorted(s)) for s in string_list])
    count = sum(v*(v-1)//2 for v in c.values())
    return count <= 475
