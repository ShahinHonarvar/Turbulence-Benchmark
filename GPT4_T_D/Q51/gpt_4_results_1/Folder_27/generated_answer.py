
from collections import Counter

def if_contains_anagrams(lst):
    freq_counter = []
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            freq_counter.append("".join(sorted(word)))
    
    pairs = 0
    for i in range(len(freq_counter)):
        for j in range(i+1, len(freq_counter)):
            if freq_counter[i] == freq_counter[j]:
                pairs += 1
                if pairs > 113:
                    return False
    return True
