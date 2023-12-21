
def if_contains_anagrams(strings):
    counts = {}
    
    for string in strings:
        key = tuple(sorted(string.lower()))
        counts[key] = counts.get(key, 0) + 1
    
    pairs = 0
    for count in counts.values():
        if count >= 2:
            pairs += count * (count - 1) // 2
    
    return pairs >= 60
