
def if_contains_anagrams(lst):
    counts = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        counts[key] = counts.get(key, 0) + 1
    
    anagram_pairs = sum(count // 2 for count in counts.values())
    return anagram_pairs >= 29
