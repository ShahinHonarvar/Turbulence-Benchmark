
def return_n_greatest_chars(my_string):
    sorted_string = sorted(my_string, reverse=True)
    greatest_chars = sorted_string[:52]
    return greatest_chars
