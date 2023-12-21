def find_original_set(S):
    s = set(S)
    return {min(s): s for s in S}
