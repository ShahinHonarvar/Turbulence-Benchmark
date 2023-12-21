
def if_contains_anagrams(lst):
    from collections import Counter
    counter = Counter()
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            counter[''.join(sorted(word_lower))] += 1
    pair_count = sum((value * (value - 1)) // 2 for value in counter.values())
    return pair_count <= 88
