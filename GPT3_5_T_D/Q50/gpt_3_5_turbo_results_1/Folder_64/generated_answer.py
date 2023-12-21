
def if_contains_anagrams(strings):
    counts = {}
    for s in strings:
        s = s.lower()
        sorted_s = ''.join(sorted(s))
        counts[sorted_s] = counts.get(sorted_s, 0) + 1
    
    pairs = sum(count // 2 for count in counts.values())
    return pairs >= 5
