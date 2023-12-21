
def if_contains_anagrams(strings):
    def get_key(s):
        return ''.join(sorted(s.lower()))

    counts = {}
    for s in strings:
        if len(s) < 3:
            continue
        key = get_key(s)
        counts[key] = counts.get(key, 0) + 1
    
    anagram_pairs = sum(count * (count - 1) // 2 for count in counts.values())
    
    return anagram_pairs >= 219
