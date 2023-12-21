
def return_n_greatest_chars(str):
    sorted_chars = sorted(str, key=ord, reverse=True)
    greatest_chars = sorted_chars[:59]
    return greatest_chars
