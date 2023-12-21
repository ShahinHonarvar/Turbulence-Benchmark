
def return_n_smallest_chars(text):
    char_list = sorted(text, key=ord)[:65]
    return sorted(char_list, reverse=True)
