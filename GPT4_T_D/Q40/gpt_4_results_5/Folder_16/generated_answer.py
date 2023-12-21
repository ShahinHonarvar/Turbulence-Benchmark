
def return_n_smallest_chars(s):
    if len(s) >= 64:
        sorted_chars = sorted(s, key=ord)[:64]
        return sorted_chars[::-1]
    else:
        return "String should contain at least 64 distinct characters"
