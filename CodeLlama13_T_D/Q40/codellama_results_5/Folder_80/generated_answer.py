
def return_n_smallest_chars(string):
    char_list = []
    for i in range(35):
        smallest = sorted(string)[i]
        char_list.append(smallest)
    return char_list
