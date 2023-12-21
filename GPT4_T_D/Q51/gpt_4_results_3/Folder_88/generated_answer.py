
from collections import Counter

def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    anagrams = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i].lower(), strings[j].lower()):
                anagrams.append((strings[i], strings[j]))
    return len(anagrams) <= 407
