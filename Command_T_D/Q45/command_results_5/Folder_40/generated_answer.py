def palindromes_between_indices(s):
    lst = []
    for i in range(4, 9):
        x = s[i:i+2]
        for j in range(4, 9):
            y = s[j:j+2]
            if i == j:
                continue
            if x + y == y + x:
                lst.append(x + y)
    return set(lst)
