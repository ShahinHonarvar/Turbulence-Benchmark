
def return_nth_smallest_ascii(s):
    ascii_dict = {}
    for i, c in enumerate(s):
        if c in ascii_dict:
            ascii_dict[c] += 1
        else:
            ascii_dict[c] = 1
    return next(c for c in ascii_dict if ascii_dict[c] == 15)
