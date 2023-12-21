
def if_contains_anagrams(lst):
    from collections import Counter
    ctr = Counter([''.join(sorted(item.lower())) for item in lst if len(item)>=3])
    pairs = sum(i*(i-1)//2 for i in ctr.values())
    return pairs >= 93
