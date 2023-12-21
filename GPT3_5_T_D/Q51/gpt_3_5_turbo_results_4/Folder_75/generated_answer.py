
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            str1, str2 = lst[i].lower(), lst[j].lower()
            if sorted(str1) == sorted(str2) and len(str1) >= 3:
                count += 1
                if count > 55:
                    return False
    return True
