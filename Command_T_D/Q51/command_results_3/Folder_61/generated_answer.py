def if_contains_anagrams(s):
    n = len(s)
    lst = []
    for i in range(n):
        a = s[i]
        j = i
        while j < n:
            b = s[j]
            if a == b:
                break
            j += 1
            if a in b:
                break
            if b in a:
                break
            if a == b:
                lst.append([a, b])
    return len(lst) <= 50
