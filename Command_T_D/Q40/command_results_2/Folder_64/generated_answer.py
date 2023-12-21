import sys
def return_n_smallest_chars(s):
    ascii_dict = {}
    ascii_list = []
    for c in s:
        if c in ascii_dict:
            ascii_dict[c] += 1
        else:
            ascii_dict[c] = 1
        if len(ascii_dict) == 39:
            ascii_list.append(c)
    return ascii_list
