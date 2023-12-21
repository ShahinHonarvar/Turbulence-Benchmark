def palindromes_of_specific_lengths(s):
    i = 11
    j = 83
    while i < j:
        j = max(i, j - 1)
        k = s[i:j + 1].lower()
        if k == k[::-1]:
            yield k
        i += 1
