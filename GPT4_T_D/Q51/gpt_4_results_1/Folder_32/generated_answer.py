
def if_contains_anagrams(lst):
    from collections import Counter

    counter = Counter([''.join(sorted(s)) for s in lst if len(s) >= 3])

    pairs_of_anagrams = sum(x*(x-1)//2 for x in counter.values())

    return pairs_of_anagrams <= 89
