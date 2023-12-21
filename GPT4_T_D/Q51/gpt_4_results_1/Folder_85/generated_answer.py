
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        count = Counter(word.lower())
        sorted_tuple = tuple(sorted(count.items()))
        if len(word) >= 3:
            if sorted_tuple in anagram_dict:
                anagram_dict[sorted_tuple].append(word)
            else:
                anagram_dict[sorted_tuple] = [word]

    count = 0
    for key in anagram_dict:
        length = len(anagram_dict[key])
        if length > 1:
            count += length*(length-1)//2
        if count > 276:
            return False
    return True
