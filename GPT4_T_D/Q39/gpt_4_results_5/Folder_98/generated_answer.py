
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=ord, reverse=True)
    if len(sorted_chars) > 68:
        sorted_chars = sorted_chars[:68]
    return sorted_chars
