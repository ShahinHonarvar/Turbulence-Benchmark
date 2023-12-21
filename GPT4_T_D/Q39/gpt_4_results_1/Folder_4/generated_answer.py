
def return_n_greatest_chars(string):
    chars_list = sorted(list(set(string)), reverse=True)
    while len(chars_list) > 90:
        chars_list.pop(-1)
    return chars_list
