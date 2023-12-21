def find_original_set(S):
    return set(sorted(set(S).intersection(*S)))
