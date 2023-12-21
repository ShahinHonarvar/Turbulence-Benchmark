def palindromes_between_indices(text):
    res = set()
    for i in range(4, 9):
        res |= set(f"".join(str(i) for i in range(i, i+i, 1)))
    return res
