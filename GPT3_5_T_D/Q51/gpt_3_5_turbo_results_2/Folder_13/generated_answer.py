
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            str1 = lst[i].lower()
            str2 = lst[j].lower()
            if sorted(str1) == sorted(str2) and len(str1) >= 3:
                count += 1
                if count > 54:
                    return False
    return True
