
def return_n_greatest_chars(string):
    char_list = list(string)
    sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)[:27]
    return "".join(sorted_list)
