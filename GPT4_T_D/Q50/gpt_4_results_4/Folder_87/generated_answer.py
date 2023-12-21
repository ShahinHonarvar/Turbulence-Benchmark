
from collections import Counter

def if_contains_anagrams(str_list):
    counter_list = [Counter(word.lower()) for word in str_list if len(word) >= 3]
    pairs_counter = 0
    for i in range(len(counter_list)):
        for j in range(i + 1, len(counter_list)):
            if counter_list[i] == counter_list[j]:
                pairs_counter += 1
    return pairs_counter >= 88
