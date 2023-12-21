
from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    words_sorted_chars = [''.join(sorted(w.lower())) for w in list_of_strings if len(w) >= 3]
    count_dict = defaultdict(int)
    for word in words_sorted_chars:
        count_dict[word] += 1
    number_of_pairs = sum((i*(i-1))//2 for i in count_dict.values())
    return number_of_pairs <= 289
