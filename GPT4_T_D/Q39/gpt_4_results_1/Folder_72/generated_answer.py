
def return_n_greatest_chars(char_string):
    sorted_string = sorted(char_string, reverse=True)
    greatest_chars = sorted_string[:37]
    return greatest_chars
