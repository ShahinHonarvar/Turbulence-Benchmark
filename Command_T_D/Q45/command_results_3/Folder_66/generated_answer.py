def palindromes_between_indices(s):
    lst = set()
    for i in range(len(s) - 5):
        a = s[i:i + 5]
        b = s[i:i + 6]
        if len(a) == len(b) == 5 and set(a.lower()) == set(b.lower()):
            lst.add(a)
            lst.add(b)
    return lst
