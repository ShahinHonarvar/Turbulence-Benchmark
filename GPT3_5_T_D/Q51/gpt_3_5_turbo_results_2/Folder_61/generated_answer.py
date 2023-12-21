
def if_contains_anagrams(strings):
    import collections
    
    counter = collections.Counter()
    
    for s in strings:
        key = ''.join(sorted(s.lower())).strip()
        counter[key] += 1
    
    anagrams = sum(i * (i - 1) // 2 for i in counter.values())
    
    return anagrams <= 50
