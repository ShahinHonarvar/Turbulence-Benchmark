def palindromes_between_indices(s):
    res = set()
    for i in range(3, min(len(s) - 1, 5) + 1):
        for j in range(i, i + i):
            lst = s[j:j + i].lower()
            if lst[0] == lst[-1] and lst[0] == lst[i - 1]:
                res.add(lst)
    return res
