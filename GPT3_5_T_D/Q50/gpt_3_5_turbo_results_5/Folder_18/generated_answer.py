
from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            count1 = Counter(lst[i].lower())
            count2 = Counter(lst[j].lower())
            
            if count1 == count2 and len(lst[i]) >= 3:
                anagram_count += 1

            if anagram_count >= 106:
                return True

    return False
