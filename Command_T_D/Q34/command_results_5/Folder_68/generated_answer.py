import sys
def find_original_set(s1, s2, s3):
    return set.intersection(s1, set.intersection(s2, s3))
