
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)

    anagrams = []
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i].lower(), lst[j].lower()):
                anagrams.append((lst[i], lst[j]))

    if len(anagrams) >= 95:
        return True
    else:
        return False
