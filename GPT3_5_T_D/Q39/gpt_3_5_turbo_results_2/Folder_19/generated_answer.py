
def return_n_greatest_chars(string):
    char_list = sorted(string, reverse=True, key=lambda c: ord(c))
    return char_list[:58]
