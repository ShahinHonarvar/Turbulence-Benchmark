
def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                pairs += 1
            if pairs >= 91:
                return True
    return False
