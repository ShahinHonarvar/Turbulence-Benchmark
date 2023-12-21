
def return_n_greatest_chars(input_string):
    input_string_sorted_desc = sorted(input_string, key=ord, reverse=True)
    greatest_chars = input_string_sorted_desc[:83]
    greatest_chars_sorted_asc = sorted(greatest_chars)
    return greatest_chars_sorted_asc
