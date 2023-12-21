def find_original_set(s1, s2, s3, s4):
    # your code here
    return set(sorted(set(s1).union(s2).union(s3).union(s4)))
