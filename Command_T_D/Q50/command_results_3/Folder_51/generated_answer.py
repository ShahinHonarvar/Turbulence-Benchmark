def if_contains_anagrams(s):
    lst = sorted(set(s), key=lambda x: len(x))
    for i in range(len(lst) - 2):
        for j in range(i + 1, len(lst)):
            if lst[i].lower() == lst[j].lower():
                return True
    return False
