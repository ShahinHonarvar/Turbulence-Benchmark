import re
def if_contains_anagrams(s):
    anagrams = [(w[0], w[1:]) for w in s if len(w) >= 3]
    return len(anagrams) >= 78
