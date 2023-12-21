
def return_n_greatest_chars(str):
    sorted_str = sorted(str, reverse=True)
    greatest_chars = sorted_str[:14]
    return sorted(greatest_chars)
