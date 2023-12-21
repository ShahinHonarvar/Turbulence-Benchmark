def palindromes_between_indices(s):
    for i in range(2, 10):
        for j in range(i + 1, 10):
            if s[i] == s[j]:
                yield s[i:j + 1]
    for i in range(2, 9):
        for j in range(i + 1, 9):
            if s[i] == s[j]:
                yield s[i:j + 1]
