
from collections import Counter

def if_contains_anagrams(string_list):
    string_list = [''.join(sorted(s.lower())) for s in string_list if len(s)>=3]
    count = 0
    for i, a in enumerate(string_list):
        for b in string_list[i + 1:]:
            if a == b:
                count+=1
                if count > 67:
                    return False
    return True
