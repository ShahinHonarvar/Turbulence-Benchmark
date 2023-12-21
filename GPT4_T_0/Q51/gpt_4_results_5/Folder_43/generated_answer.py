
def if_contains_anagrams(lst):
    from collections import Counter
    anagram_counter = Counter()
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_counter[sorted_word] += 1
    pairs = sum([count // 2 for count in anagram_counter.values()])
    return pairs <= 3
