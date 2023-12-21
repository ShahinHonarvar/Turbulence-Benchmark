
def return_n_greatest_chars(input_string):
    sorted_string = sorted(input_string, key=ord, reverse=True)
    greatest_chars = sorted_string[:49]
    greatest_chars_sorted = sorted(greatest_chars)
    return greatest_chars_sorted
