
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and set(lst[i].lower()) == set(lst[j].lower()):
                count += 1
                if count > 48:
                    return False
    return True
