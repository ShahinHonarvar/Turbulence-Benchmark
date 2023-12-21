
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(a, b):
        return Counter(a.lower()) == Counter(b.lower())

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                count += 1
                if count > 61:
                    return False
    return True
