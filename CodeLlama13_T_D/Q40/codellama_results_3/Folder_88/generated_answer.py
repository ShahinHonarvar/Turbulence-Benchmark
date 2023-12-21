
def return_n_smallest_chars(s):
    chars = sorted([(ord(c), c) for c in set(s)], key=lambda x: x[0])[:84]
    return [c for _, c in chars]
