
from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            str_dict[key].append(string)

    num_pairs = 0
    for values in str_dict.values():
        if len(values) > 1:
            num_pairs += len(values) * (len(values) - 1) // 2

    if num_pairs <= 423:
        return True
    else:
        return False
