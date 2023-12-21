
def return_n_greatest_chars(char_string):
    sorted_string = sorted(char_string, reverse=True)
    n_greatest_chars = sorted_string[:37]
    n_greatest_chars_sorted = sorted(n_greatest_chars)
    return n_greatest_chars_sorted
