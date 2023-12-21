
def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and lst[i].lower() == lst[j].lower():
                pairs += 1
                if pairs >= 8:
                    return True
    return False
