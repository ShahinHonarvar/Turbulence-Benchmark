
import collections

def if_contains_anagrams(lst):
    count = 0
    anagrams = collections.defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word] += 1
            count += anagrams[sorted_word] - 1
    return count <= 55
