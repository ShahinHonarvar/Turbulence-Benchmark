
def find_original_set(s1, s2, s3, s4, s5, s6, s7):
    # initialize an empty set
    original_set = set()
    # add each argument to the original set
    for arg in [s1, s2, s3, s4, s5, s6, s7]:
        original_set.update(arg)
    return original_set
