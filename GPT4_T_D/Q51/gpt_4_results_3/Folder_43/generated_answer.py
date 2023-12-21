
from collections import Counter

def if_contains_anagrams(list_of_strings):
    sorted_list = [''.join(sorted(word.lower())) for word in list_of_strings if len(word) >= 3]
    count = Counter(sorted_list)
    pairs = sum(1 for text, number in count.items() if number > 1)
    return pairs <= 3
