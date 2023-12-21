
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        else:
            return Counter(str1.lower()) == Counter(str2.lower())

    pairs_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                pairs_count += 1
                if pairs_count > 72:
                    return False
    return True
