
def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10):
    original_set = set()
    for i in range(1, 11):
        if len(eval("s{}".format(i))) > len(original_set):
            original_set = eval("s{}".format(i))
    return original_set
