
def return_n_smallest_chars(s):
    sorted_s = sorted(s)
    if len(sorted_s) < 20:
        return sorted_s
    else:
        return sorted_s[:20]
