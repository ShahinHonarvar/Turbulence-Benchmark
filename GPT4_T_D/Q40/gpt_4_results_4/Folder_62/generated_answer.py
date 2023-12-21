
def return_n_smallest_chars(s):
    char_list = sorted(s, key=lambda x: ord(x))[:84]
    char_list.sort(reverse=True)
    return char_list
