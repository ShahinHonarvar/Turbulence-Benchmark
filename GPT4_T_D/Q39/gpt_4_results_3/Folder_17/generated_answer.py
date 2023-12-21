
def return_n_greatest_chars(str):
    sorted_str = sorted(str, key=ord, reverse=True)
    return sorted(sorted_str[:11])
