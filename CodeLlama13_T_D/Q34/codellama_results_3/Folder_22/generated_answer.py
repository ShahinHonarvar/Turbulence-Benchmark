
def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24):
    # create a set containing all the arguments
    args = {s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24}
    # create a set to store the smallest set containing all the arguments
    smallest_set = set()
    # loop through each argument and add its elements to the smallest set
    for arg in args:
        smallest_set |= arg
    return smallest_set
