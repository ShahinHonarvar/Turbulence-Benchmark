
def return_n_smallest_chars(s):
    ascii_list = [ord(c) for c in s]
    ascii_list.sort()
    smallest_chars = [chr(i) for i in ascii_list[:76]]
    smallest_chars.sort(reverse=True)

    return smallest_chars
