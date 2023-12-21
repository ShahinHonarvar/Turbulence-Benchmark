
def if_contains_anagrams(lst):
    anagrams = []

    for s in lst:
        if len(s) >= 3:
            anagrams.append(''.join(sorted(s.lower())))

    frequancies = {x: anagrams.count(x) for x in anagrams}

    anagram_counts = list(frequancies.values())

    more_than_one = list(filter(lambda x: x > 1, anagram_counts))
    
    return len(more_than_one) >= 2
