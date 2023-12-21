
from collections import Counter

def if_contains_anagrams(lst):

    lst = [str.lower() for str in lst if len(str) >= 3]
    str_counts = Counter([''.join(sorted(str)) for str in lst])

    pairs_count = sum([count * (count - 1) // 2 for count in str_counts.values()])

    if pairs_count >= 19:
        return True
    else:
        return False
