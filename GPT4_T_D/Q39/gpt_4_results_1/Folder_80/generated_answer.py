
def return_n_greatest_chars(char_string):
    greatest_chars = sorted(char_string, key=ord, reverse=True)[:35]
    return sorted(greatest_chars)
