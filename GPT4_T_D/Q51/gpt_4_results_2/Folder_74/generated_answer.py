
from collections import defaultdict

def if_contains_anagrams(lst):
    def make_sortable(word):
        return "".join(sorted(word.lower()))

    sorted_words = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_words[make_sortable(word)].append(word)

    total_pairs = sum(len(values)*(len(values)-1)/2 for values in sorted_words.values())
    return total_pairs <= 57
