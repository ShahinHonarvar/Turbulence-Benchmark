
def return_n_smallest_chars(char_string):
    sorted_string = sorted(char_string, key=lambda x: -ord(x))
    return sorted_string[:61]
