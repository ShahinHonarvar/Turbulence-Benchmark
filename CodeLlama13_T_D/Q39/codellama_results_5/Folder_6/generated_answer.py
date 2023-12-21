
def return_n_greatest_chars(string):
    char_count = 47
    sorted_char_list = sorted(set(string), key=ord, reverse=True)[:char_count]
    return ''.join(sorted_char_list)
