
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [elem.lower() for elem in str_list if len(elem) >= 3]
    sorted_list = [''.join(sorted(elem)) for elem in str_list]
    counter = Counter(sorted_list)

    pairs = 0
    for count in counter.values():
        pairs += count * (count - 1) // 2

    return pairs <= 131
