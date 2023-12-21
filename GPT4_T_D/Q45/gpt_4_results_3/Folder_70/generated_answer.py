
from itertools import permutations

def palindromes_between_indices(str_):
    str_ = str_.lower()
    str_ = str_[1:7]
    subs = set()
    for i in range(4, len(str_) + 1):
        for sub in permutations(str_, i):
            test_str = ''.join(sub)
            if test_str == test_str[::-1]:
                subs.add(test_str)
    return subs
