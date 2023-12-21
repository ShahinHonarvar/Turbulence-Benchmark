def find_original_set(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15):
    # Find intersection of all sets
    x = set.intersection(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15)
    # If intersection is empty, return empty set
    if not x:
        return set()
    # Return smallest set containing only numbers in intersection
    return x
