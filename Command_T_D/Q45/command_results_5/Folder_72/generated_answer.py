def palindromes_between_indices(s):
    if not s:
        return set()
    letters = set(s[1:7])
    if not letters:
        return set()
    for i in range(1, 7):
        for j in range(i + 1, 7):
            if i >= j:
                continue
            if s[i:j] in letters:
                yield s[i:j]
    for i in range(2, 6):
        for j in range(i + 1, 6):
            if i >= j:
                continue
            if s[i:j] in letters:
                yield s[i:j]
