
from collections import Counter

def if_contains_anagrams(lst_str):
    def check_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    lst_str = [x.lower() for x in lst_str]
    pairs = 0

    for i in range(len(lst_str)):
        for j in range(i + 1, len(lst_str)):
            if len(lst_str[i]) >= 3 and len(lst_str[j]) >= 3:
                if check_anagram(lst_str[i], lst_str[j]):
                    pairs += 1
    
    if pairs <= 65:
        return True
    else:
        return False
