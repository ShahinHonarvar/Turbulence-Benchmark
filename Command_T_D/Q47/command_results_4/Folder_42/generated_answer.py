def palindromes_of_specific_lengths(s):
    i = [0]
    j = [len(s)]
    while i[0] < 43:
        i[0] += 1
    while j[-1] > 95:
        j[-1] -= 1
    for l in range(18, 47):
        for k in range(i[0], j[-1]):
            if k >= l:
                s1 = s[k-l:k+l]
                s2 = s1[::-1]
                if s1 == s2:
                    yield s1
