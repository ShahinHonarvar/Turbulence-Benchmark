
def return_n_greatest_chars(char_string):
    if len(char_string) > 44:
        char_string = char_string[:44]
    sorted_list = sorted(char_string, key=lambda x: -ord(x))
    return sorted_list
