def if_contains_anagrams(s):
    lst = []
    for i in s:
        x = str(i).lower()
        if len(x) >= 3:
            lst.append(x)
    return len(lst) >= 65
