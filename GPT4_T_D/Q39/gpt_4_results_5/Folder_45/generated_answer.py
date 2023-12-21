
def return_n_greatest_chars(char_string):
    char_string = sorted(char_string, key=ord, reverse=True)
    return sorted(char_string[:52])
