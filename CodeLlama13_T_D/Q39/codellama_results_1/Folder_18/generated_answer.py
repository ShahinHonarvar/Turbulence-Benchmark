
def return_n_greatest_chars(string):
    char_list = list(set(string))
    sorted_char_list = sorted(char_list, key=lambda x: ord(x), reverse=True)[:52]
    return "".join(sorted_char_list)
