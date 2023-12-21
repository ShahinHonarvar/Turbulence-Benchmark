
def return_n_greatest_chars(string):
    char_list = list(set(string))
    if len(char_list) < 32:
        return 'The string must contain at least 32 different characters.'
    char_list.sort(key=ord, reverse=True)
    return char_list[:32]
