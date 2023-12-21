
def return_n_smallest_chars(s):
    if len(s) > 76:
        s = ''.join(sorted(s, reverse=True))[:76]
    else:
        s = ''.join(sorted(s, reverse=True))
    return list(s)
