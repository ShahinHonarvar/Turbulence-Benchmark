
def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=ord, reverse=True)
    greatest_chars = sorted_string[:6]
    return greatest_chars
