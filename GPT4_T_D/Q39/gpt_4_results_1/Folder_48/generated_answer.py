
def return_n_greatest_chars(str):
    sorted_chars = sorted(str, key=ord, reverse=True)[:12]
    return sorted(sorted_chars)
