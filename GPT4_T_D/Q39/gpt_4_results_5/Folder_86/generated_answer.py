
def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string, key=ord, reverse=True)
    greatest_chars = sorted_chars[:34]
    greatest_chars.sort()
    return greatest_chars
