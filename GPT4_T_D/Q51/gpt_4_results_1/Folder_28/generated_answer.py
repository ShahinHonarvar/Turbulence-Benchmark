
from collections import Counter

def if_contains_anagrams(lst):
    anagrms = {}
    for word in lst:
        word = word.lower()
        if len(word) >=3:
            sorted_word = ''.join(sorted(word))
            anagrms[sorted_word] = anagrms.get(sorted_word,0) + 1
    pairs = sum(val*(val-1)//2 for val in anagrms.values())
    return pairs <= 78
