
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                count += 1
                if count >= 8:
                    return True
    return False
