
def return_n_smallest_chars(s):
    char_list = [char for char in s if ord(char) < 123]
    if len(char_list) >= 38:
        sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)[:38]
    else:
        sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)
    return sorted_list
