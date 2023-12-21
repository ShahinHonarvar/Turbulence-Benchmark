
def return_n_smallest_chars(string):
    char_list = sorted([char for char in string if char.isalpha()], key=ord)
    return char_list[:24]
