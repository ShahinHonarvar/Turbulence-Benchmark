
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)
    
    for s in lst:
        key = "".join(sorted(s.lower()))
        if len(key) >= 3:
            anagrams[key].append(s)
            
    pairs = sum(len(vs)*(len(vs)-1)//2 for vs in anagrams.values())
    
    return pairs >= 46
