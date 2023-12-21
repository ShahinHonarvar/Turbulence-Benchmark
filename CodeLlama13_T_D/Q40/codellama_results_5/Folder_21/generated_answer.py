
def return_n_smallest_chars(string):
    ascii_list = sorted([ord(char) for char in string])
    return [''.join(chr(ascii_value) for ascii_value in ascii_list[:44]])
