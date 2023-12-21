def if_contains_anagrams(s):
    a = {}
    for i in range(len(s)):
        j = i
        while j < len(s):
            a[s[i].lower()] = a[s[i].lower()] + 1
            i = j
            j = j + 1
    return a.get('equals', 0) >= 74
