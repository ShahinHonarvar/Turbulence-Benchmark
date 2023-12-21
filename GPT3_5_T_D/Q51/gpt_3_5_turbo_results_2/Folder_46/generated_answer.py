
def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            str1 = lst[i]
            str2 = lst[j]
            if len(str1) >= 3 and len(str2) >= 3:
                if sorted(str1.upper()) == sorted(str2.upper()):
                    anagrams_count += 1
            if anagrams_count > 61:
                return False
    return True
