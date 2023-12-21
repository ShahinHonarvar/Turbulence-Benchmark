
from collections import defaultdict

def if_contains_anagrams(str_list):
    str_count = defaultdict(int)
    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            str_count[sorted_word] += 1
            
    pairs = sum([v*(v-1)//2 for v in str_count.values() if v > 1])
    
    return pairs <= 47
