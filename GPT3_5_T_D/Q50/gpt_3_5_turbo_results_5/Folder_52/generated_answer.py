
def if_contains_anagrams(strings):
    counts = {}
    
    for string in strings:
        key = ''.join(sorted(string.lower()))
        
        if len(key) < 3:
            continue
        
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    
    pairs = sum(count * (count - 1) // 2 for count in counts.values())
    
    if pairs >= 58:
        return True
    
    return False
