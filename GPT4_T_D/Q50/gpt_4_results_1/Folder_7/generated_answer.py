
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    def count_anagram_pairs(words):
        d = defaultdict(list)
        for word in words:
            d[''.join(sorted(word.lower()))].append(word)
        return sum(len(value)*(len(value)-1)//2 for key,value in d.items() if len(key) >= 3)


    return count_anagram_pairs(lst) >= 178
