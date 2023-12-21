def find_original_set(s):
    s = set(s)
    s = {x for x in range(len(s) + 1)}
    s = {str(x): x for x in range(len(s) + 1)}
    return s
