
def return_n_smallest_chars(s):
    char_list = sorted([c for c in s if ord(c) < 128], key=ord)[:32]
    return ''.join(char_list)
