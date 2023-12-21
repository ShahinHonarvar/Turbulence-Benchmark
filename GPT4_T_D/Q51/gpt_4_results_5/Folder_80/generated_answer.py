
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    cnt = 0
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue

        for j in range(i+1, len(lst)):
            if len(lst[j]) < 3:
                continue
            
            if is_anagram(lst[i], lst[j]):
                cnt += 1

                if cnt > 255:
                    return False
    return True
