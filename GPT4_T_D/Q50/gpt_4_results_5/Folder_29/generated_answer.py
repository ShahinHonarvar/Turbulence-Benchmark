
from collections import defaultdict

def if_contains_anagrams(lst):
    count_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            count_dict[sorted_word].append(word)
            
    anagram_pairs = sum([len(values)*(len(values)-1)//2 for values in count_dict.values() if len(values) > 1])
    
    if anagram_pairs >= 35: 
        return True
    return False
