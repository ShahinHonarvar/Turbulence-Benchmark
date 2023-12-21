
from collections import Counter

def if_contains_anagrams(str_list):
    count = 0
    str_freq = ["".join(sorted(word.lower())) for word in str_list if len(word) >= 3]
    for word_freq in Counter(str_freq).values():
        count += (word_freq * (word_freq - 1)) // 2 
    if count <= 20:
        return True
    else:
        return False
