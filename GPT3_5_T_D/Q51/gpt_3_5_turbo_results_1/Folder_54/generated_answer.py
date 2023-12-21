 
def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()) and len(lst[i]) >= 3:
                pairs += 1
                if pairs > 39:
                    return False
    return True
