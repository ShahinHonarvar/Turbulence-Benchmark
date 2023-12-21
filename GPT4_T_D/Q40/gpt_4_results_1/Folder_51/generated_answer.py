
def return_n_smallest_chars(s):
    if len(s) < 45:
        raise ValueError("The string should have at least 45 distinct characters")
    else:
        sorted_s = sorted(s, key=ord)
        smallest_chars = sorted_s[:45]
        return sorted(smallest_chars, reverse=True)
