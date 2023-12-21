
from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    counter_list = [Counter(w.lower()) for w in lst if len(w) >= 3]
    len_counter_list = len(counter_list)
    for i in range(len_counter_list):
        for j in range(i + 1, len_counter_list):
            if counter_list[i] == counter_list[j]:
                anagram_count += 1
    return anagram_count <= 92
