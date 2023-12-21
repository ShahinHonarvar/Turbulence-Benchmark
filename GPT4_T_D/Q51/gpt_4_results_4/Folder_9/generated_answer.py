
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    count = 0
    processed = defaultdict(int)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if is_anagram(lst[i], lst[j]):
                key = tuple(sorted([lst[i], lst[j]]))
                if processed[key] == 0:
                    count += 1
                    processed[key] = 1
                    if count > 475:
                        return False
    return True
