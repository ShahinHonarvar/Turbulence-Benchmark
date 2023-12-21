
from collections import defaultdict
def if_contains_anagrams(str_lst):
    anagram_dict = defaultdict(set)

    for word in str_lst:
        word = word.lower()
        if len(word) >= 3:
            key = "".join(sorted(word))
            anagram_dict[key].add(word)
            
    anagram_pairs = sum([len(val)*(len(val)-1)//2 for val in anagram_dict.values()])
    
    return anagram_pairs <= 26
