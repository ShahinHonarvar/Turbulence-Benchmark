
from collections import defaultdict

def if_contains_anagrams(str_list):
    count = 0
    frequency = defaultdict(int)
    
    for string in str_list:
        sorted_word = ''.join(sorted(string.lower()))
        frequency[sorted_word] += 1
    
    for count in frequency.values():
        if count >= 2:
            pairs = count * (count - 1) // 2
            count += pairs
    
    return True if count >= 79 else False
