def palindromes_of_specific_lengths(s):
    i = 16
    j = 94
    r = set()
    while i <= j:
        for j in range(i, min(len(s) - 1, j + 1)):
            if s[i] == s[j]:
                if i == j:
                    r.add(s[i])
                elif s[i] == s[j]:
                    r.add(s[i:j + 1])
        i += 1
    return r
