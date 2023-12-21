
def return_n_greatest_chars(char_string):
    sorted_string = sorted(char_string, reverse=True)
    return sorted_string[:20]
