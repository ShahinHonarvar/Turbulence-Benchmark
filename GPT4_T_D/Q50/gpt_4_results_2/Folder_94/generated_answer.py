
def if_contains_anagrams(lst):
    from collections import Counter
    all_anagrams = []
    for i in lst:
        if len(i) >= 3:
            all_anagrams.append(''.join(sorted(i.lower())))

    counter = Counter(all_anagrams)
    pairs_of_anagrams = 0

    for value in counter.values():
        pairs_of_anagrams += (value * (value-1)) //2

    if pairs_of_anagrams >= 46:
        return True
    else:
        return False
