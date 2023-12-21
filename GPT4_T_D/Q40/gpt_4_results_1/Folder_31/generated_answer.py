
def return_n_smallest_chars(s):
    if len(s) < 70:
        return "String does not have enough distinct characters"
    else:
        sorted_chars = sorted(s)
        sorted_chars_70 = sorted_chars[:70]
        return sorted(sorted_chars_70, reverse=True)
