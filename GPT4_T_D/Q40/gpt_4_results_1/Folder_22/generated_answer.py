
def return_n_smallest_chars(s):
    if len(s) < 76:
        raise ValueError("The input string should have at least 76 distinct characters.")
    else:
        sorted_s = sorted(s, key=ord)
        return sorted_s[:76]
