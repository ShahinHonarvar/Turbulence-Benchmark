
def return_n_greatest_chars(char_string):
    sorted_string = sorted(char_string, key=lambda c: ord(c))
    return sorted_string[-19:]
