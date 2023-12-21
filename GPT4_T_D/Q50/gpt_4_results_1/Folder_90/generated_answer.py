
def if_contains_anagrams(arr):
    from collections import defaultdict
    
    map = defaultdict(list)
    for text in arr: 
        if len(text) >= 3: 
            map[str(sorted(text.lower()))].append(text) 
    
    pairs_number = 0
    for key in map: 
        pairs_number += len(map[key])*(len(map[key])-1)//2 
    
    if pairs_number >= 177: 
        return True
    else: 
        return False
