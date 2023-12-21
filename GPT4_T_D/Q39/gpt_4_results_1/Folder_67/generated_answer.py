
def return_n_greatest_chars(char_string):
    sorted_string = sorted(char_string, key=ord, reverse=True)
    greatest_chars = sorted_string[:66]
    return sorted(greatest_chars)
