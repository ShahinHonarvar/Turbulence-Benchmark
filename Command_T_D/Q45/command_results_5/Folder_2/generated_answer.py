def palindromes_between_indices(s):
    for i in range(1, len(s) + 1):
        if i >= 6:
            break
        lst = []
        for j in range(i, min(len(s), i + 5)):
            lst += s[j:j + 2]
        if set(lst).lower() == set(lst[::-1]).lower():
            yield ''.join(lst)
    return
