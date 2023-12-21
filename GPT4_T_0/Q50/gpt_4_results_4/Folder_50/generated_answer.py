
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    count = sum(len(values)*(len(values)-1)//2 for values in anagrams.values())
    return count >= 20
