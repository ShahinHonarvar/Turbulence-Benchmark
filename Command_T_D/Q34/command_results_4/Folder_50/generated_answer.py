def find_original_set(arg):
    s = set()
    for i in range(len(arg)):
        s.update(arg[i])
    return s
