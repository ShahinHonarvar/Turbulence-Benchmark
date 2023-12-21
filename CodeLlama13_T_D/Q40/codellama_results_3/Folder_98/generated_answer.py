
def return_n_smallest_chars(s):
    char_count = len(s)
    if char_count <= 68:
        return list(sorted(set(s), key=ord))
    else:
        return sorted(list(set(s)), key=ord)[0:68]
