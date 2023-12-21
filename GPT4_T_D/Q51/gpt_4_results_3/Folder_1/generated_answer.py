
def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            a, b = lst[i].lower(), lst[j].lower()
            if len(a) >= 3 and sorted(a) == sorted(b):
                pairs += 1
                if pairs > 30:
                    return False
    return True
