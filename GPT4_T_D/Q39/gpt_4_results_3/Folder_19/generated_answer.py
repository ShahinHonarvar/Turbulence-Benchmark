
def return_n_greatest_chars(s):
    if len(s) < 58:
        raise ValueError("You need to provide at least 58 distinct characters.")
    sorted_chars = sorted(s, key=ord, reverse=True)
    return sorted(sorted_chars[:58])
