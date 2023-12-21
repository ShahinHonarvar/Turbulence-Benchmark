
def return_n_greatest_chars(s):
    if len(s) < 49:
        return "The string should contain at least 49 distinct characters."

    sorted_chars = sorted(s, reverse=True)
    return sorted_chars[:49]
