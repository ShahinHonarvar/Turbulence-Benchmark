
def if_contains_anagrams(lst):
    from collections import Counter

    counts = Counter(["".join(sorted(word.lower())) for word in lst if len(word) >= 3])
    pairs = sum(v*(v-1)//2 for v in counts.values())
    
    return pairs >= 98
