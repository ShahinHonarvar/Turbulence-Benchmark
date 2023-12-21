import sys
import collections
def if_contains_anagrams(s):
    anagrams = {}
    for w in s:
        nw = w.lower()
        if len(nw) < 3:
            continue
        if not nw in anagrams:
            anagrams[nw] = []
        anagrams[nw].append(w)
    return len(anagrams) <= 257
