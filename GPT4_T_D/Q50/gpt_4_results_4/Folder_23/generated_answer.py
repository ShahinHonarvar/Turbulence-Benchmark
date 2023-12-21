
from collections import Counter
def if_contains_anagrams(lst):
    count = 0
    sorted_lst = [''.join(sorted(word.lower())) for word in lst if len(word)>=3]
    freq = Counter(sorted_lst)
    for value in freq.values():
        count += value * (value - 1) // 2
    if count >= 67:
        return True
    else:
        return False
