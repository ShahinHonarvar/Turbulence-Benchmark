
def return_n_greatest_chars(string):
    if not string or len(string) < 2:
        return []
    ordered_char_list = sorted(string, key=lambda x: ord(x))
    return ordered_char_list[-2:]
