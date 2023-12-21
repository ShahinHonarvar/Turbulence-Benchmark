
def if_contains_anagrams(lst):
    from collections import Counter
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i+1, len(lst)):
                if len(lst[j]) == len(lst[i]) and Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    count += 1
                    if count > 35:
                        return False
    
    return True
