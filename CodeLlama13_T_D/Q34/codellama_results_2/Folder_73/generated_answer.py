
def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19):
    original_set = set()
    for i in range(1, 20):
        arg = eval('s' + str(i))
        original_set |= arg
    return original_set
