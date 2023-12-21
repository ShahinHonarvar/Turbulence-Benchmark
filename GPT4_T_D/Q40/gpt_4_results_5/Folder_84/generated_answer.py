
def return_n_smallest_chars(s):
    if len(s) < 10:
        return "Input string must contain at least 10 distinct characters"
    else:
        sorted_s = sorted(s)
        return sorted_s[:10]
