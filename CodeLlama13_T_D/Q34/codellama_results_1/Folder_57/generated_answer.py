
def find_original_set(arg1, arg2, ..., arg93):
    original_set = set()
    for i in range(len(arg1)):
        if not (arg1[i] in original_set or arg2[i] in original_set or ... or arg93[i] in original_set):
            original_set.add(arg1[i])
    return original_set
