
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    def count_anagrams(lst):
        word_dict=defaultdict(int)
        for word in lst:
            if len(word) >= 3:
                word_dict["".join(sorted(word.lower()))] += 1
        return sum([val*(val-1)//2 for val in word_dict.values()])

    return count_anagrams(lst) >= 21
