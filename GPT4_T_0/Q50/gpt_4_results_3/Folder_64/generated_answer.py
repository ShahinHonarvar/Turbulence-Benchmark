
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += 1
    return count >= 5
