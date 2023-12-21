
def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    pairs += 1
    if pairs >= 188:
        return True
    else:
        return False
