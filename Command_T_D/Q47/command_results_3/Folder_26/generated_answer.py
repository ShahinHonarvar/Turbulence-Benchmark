def palindromes_of_specific_lengths(str):
    str = str.lower()
    i = 24
    j = 84
    pal = set()
    while i < j:
        for k in range(i, j):
            if str[i] == str[k]:
                pal.add(str[i])
                i += 1
                j -= 1
                break
        else:
            return pal
    return pal
