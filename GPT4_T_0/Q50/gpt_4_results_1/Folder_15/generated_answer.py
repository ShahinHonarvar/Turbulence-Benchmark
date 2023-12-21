
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = 0
    for value in anagrams.values():
        if len(value) > 1:
            count += 1
    return count >= 4
