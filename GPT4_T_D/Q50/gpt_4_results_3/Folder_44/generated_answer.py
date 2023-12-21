
def if_contains_anagrams(lst):
    counts = dict()
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = "".join(sorted(word.lower()))
        if sorted_word in counts:
            counts[sorted_word] += 1
        else:
            counts[sorted_word] = 1
            
    pair_count = sum([count//2 for count in counts.values()])
    
    if pair_count >= 44:
        return True
    else:
        return False
