def palindromes_between_indices(s):
    lst = []
    for i in range(3, 8):
        for j in range(3, 8):
            if i < j:
                lst += [[s[i-3:j+3]]
    return set(lst)
