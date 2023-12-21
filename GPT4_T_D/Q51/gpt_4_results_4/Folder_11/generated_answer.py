
from collections import defaultdict

def if_contains_anagrams(word_list):
    word_list = ["".join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    word_map = defaultdict(int)
    
    for word in word_list:
        word_map[word] += 1
    
    count = 0
    for val in word_map.values():
        count += ((val*(val-1))//2)
    
    return count <= 41
