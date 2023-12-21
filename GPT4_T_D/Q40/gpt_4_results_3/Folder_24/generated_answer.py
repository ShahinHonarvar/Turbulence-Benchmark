
def return_n_smallest_chars(char_string):
    char_string = sorted(char_string, key=lambda x: ord(x))
    smallest_chars = char_string[:32]
    return smallest_chars[::-1]
