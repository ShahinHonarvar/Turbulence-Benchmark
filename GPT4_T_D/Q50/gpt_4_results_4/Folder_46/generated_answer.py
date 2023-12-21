
from collections import defaultdict

def if_contains_anagrams(lst):
    str_dict = defaultdict(list)
    for i in lst:
        i_lower = i.lower()
        if len(i_lower) >= 3:
            str_dict[''.join(sorted(i_lower))].append(i)

    pair_count = 0
    for key in str_dict:
        n = len(str_dict[key])
        pair_count += n * (n - 1) // 2

    return pair_count >= 38
