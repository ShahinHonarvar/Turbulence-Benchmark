
def if_contains_anagrams(lst):
    from collections import Counter
    anagrams = []
    for word in lst:
        if len(word) > 2:
            word = word.lower()
            anagrams.append(''.join(sorted(word)))
    counter = Counter(anagrams)
    return sum([count*(count-1)//2 for count in counter.values()]) >= 246
