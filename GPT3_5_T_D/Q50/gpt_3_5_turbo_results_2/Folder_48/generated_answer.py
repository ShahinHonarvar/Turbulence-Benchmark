 
from collections import Counter

def if_contains_anagrams(strings):
    def is_anagram(a, b):
        a = a.lower()
        b = b.lower()
        return Counter(a) == Counter(b) and len(a) >= 3 and len(b) >= 3

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 219:
                    return True
    return False
