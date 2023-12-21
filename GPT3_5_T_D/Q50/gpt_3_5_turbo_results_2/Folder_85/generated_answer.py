
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(string1, string2):
        return Counter(string1.lower()) == Counter(string2.lower())

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                count += 1

    return count >= 73
