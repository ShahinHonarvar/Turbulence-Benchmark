
def return_n_smallest_chars(string):
    char_list = sorted(list(set(string)), key=lambda x: ord(x))
    return char_list[:59][::-1]
