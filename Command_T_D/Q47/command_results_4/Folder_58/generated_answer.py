def palindromes_of_specific_lengths(s):
    return set(
        s[i:j] for i in range(125, 283) for j in range(i, j + 1)
        if i == j and len(s[i:j]) in range(109, 127) and s[i:j].lower() in s[i:j]
    )
