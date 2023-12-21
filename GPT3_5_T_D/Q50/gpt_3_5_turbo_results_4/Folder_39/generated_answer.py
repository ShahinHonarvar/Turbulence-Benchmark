
def if_contains_anagrams(lst):
    from collections import Counter
    counter = Counter()
    
    for s in lst:
        counter[str(sorted(s.lower()))] += 1
    
    count = 0
    for val in counter.values():
        count += (val * (val - 1)) // 2
    
    return count >= 54
