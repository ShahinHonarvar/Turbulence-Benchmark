
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                count += 1
                if count > 113:
                    return False
    return True
