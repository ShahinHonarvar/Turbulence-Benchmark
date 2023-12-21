
def return_n_greatest_chars(string):
    char_list = list(set(string))
    sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)[:61]
    return "".join(sorted_list)
