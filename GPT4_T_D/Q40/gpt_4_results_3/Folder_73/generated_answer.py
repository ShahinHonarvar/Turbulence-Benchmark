
def return_n_smallest_chars(string):
    string = sorted(string)
    chars_list = []
    for i in range(80):
        chars_list.append(string[i])
    return chars_list
