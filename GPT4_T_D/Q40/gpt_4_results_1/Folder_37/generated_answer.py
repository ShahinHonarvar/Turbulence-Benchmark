
def return_n_smallest_chars(s):
    ascii_list = [ord(c) for c in s]
    ascii_list.sort()
    smallest_chars_list = [chr(i) for i in ascii_list[:26]]
    smallest_chars_list.sort(reverse=True)
    return smallest_chars_list
