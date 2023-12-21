
def if_contains_anagrams(lst):
    pair_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    pair_count += 1
                    if pair_count > 85:
                        return False
    return True
