
def if_contains_anagrams(strings):
    import collections
    counter = collections.Counter()
    pairs = 0
    
    for string in strings:
        if len(string) >= 3:
            normalized = ''.join(sorted(string.lower()))
            counter[normalized] += 1
            pairs += counter[normalized] - 1
    
    return pairs <= 131
