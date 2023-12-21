def find_original_set(s):
    return set(sorted(set.intersection(*s)))
