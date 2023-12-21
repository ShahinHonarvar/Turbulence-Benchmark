
def if_contains_anagrams(strings):
    from collections import defaultdict

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    counts = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            counts["".join(sorted(string.lower()))].append(string)

    pairs = 0
    for key in counts:
        pairs += len(counts[key]) * (len(counts[key]) - 1) / 2
        
    return pairs >= 77
