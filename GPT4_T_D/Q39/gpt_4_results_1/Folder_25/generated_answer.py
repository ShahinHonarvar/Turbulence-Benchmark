
def return_n_greatest_chars(char_string):
    char_string_sorted_desc = sorted(char_string, reverse=True)
    greatest_chars = char_string_sorted_desc[:29]
    ascending_greatest_chars = sorted(greatest_chars)
    return ascending_greatest_chars
