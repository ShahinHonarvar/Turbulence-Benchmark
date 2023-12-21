def find_original_set(S):
    s = set()
    for s1 in S:
        for s2 in S:
            for s3 in S:
                s |= s1 | s2 | s3
    return s
