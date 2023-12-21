
from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    anagrams = {}
    for string in lst:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(string)
        else:
            anagrams[sorted_str] = [string]

    for key in anagrams:
        count = len(anagrams[key])
        pairs += count*(count-1)//2

    if pairs <= 98:
        return True
    return False
