def find_original_set(S):
    M = set()
    for s in S:
        for e in s:
            M.add(e)
    return M
