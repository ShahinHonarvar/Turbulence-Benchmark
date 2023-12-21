
def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string, key=ord, reverse=True)[:20]
    return sorted(sorted_chars)
