
def if_contains_anagrams(lst):
    from collections import Counter

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    count += 1

    if count <= 64:
        return True
    else:
        return False
