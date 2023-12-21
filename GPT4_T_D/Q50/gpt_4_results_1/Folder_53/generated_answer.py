
from collections import Counter

def if_contains_anagrams(lst):
    # create a list of sorted word
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    # count of all words
    word_counts = Counter(sorted_words)
    # only consider counts > 1 (for pair) and sum them
    pairs_count = sum([count // 2 for count in word_counts.values() if count > 1])
    # return if pairs count is >= 11
    return pairs_count >= 11
