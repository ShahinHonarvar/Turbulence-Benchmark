def if_contains_anagrams(list1):
    d = {}
    for i in list1:
        s = str(i).lower()
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    return len(d) <= 206
