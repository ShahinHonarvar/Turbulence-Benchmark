
def if_contains_anagrams(lst):
    from collections import Counter
    count = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if (Counter(lst[i].lower()) == Counter(lst[j].lower())) and len(lst[i]) >= 3:
                count += 1
                if count > 44:
                    return False
    return True
