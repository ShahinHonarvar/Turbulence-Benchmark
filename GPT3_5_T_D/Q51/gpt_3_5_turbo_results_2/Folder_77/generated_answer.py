
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    count += 1
                    if count > 17:
                        return False
    return True
