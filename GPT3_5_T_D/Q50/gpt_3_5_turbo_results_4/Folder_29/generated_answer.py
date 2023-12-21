
def if_contains_anagrams(lst):
    anagrams = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    anagrams += 1
                    if anagrams >= 35:
                        return True
    return False
