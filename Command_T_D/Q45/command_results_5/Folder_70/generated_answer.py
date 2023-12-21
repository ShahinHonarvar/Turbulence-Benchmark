def palindromes_between_indices(s):
    lst = ['']
    for i in range(len(s) - 1):
        lst.append(lst[-1] + s[i])
    return set(x for x in lst if x[::-1] == x)
