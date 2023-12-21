
def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8):
    sets = set()
    for s in (s1, s2, s3, s4, s5, s6, s7, s8):
        sets.add(set(s))
    return sets.pop()
