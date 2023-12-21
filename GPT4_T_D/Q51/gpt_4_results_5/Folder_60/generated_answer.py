
from collections import defaultdict

def if_contains_anagrams(words): 
    word_dict = defaultdict(int)
    for word in words:
        word_lower = word.lower()
        if len(word_lower)>=3:
            sorted_word = "".join(sorted(word_lower))
            word_dict[sorted_word] += 1
    count = sum([val*(val-1)//2 for val in word_dict.values()]) 
    if count <= 77:
        return True
    else: 
        return False
