
def return_n_greatest_chars(string):
    char_count = 80
    sorted_chars = sorted(string, key=lambda x: ord(x))
    return sorted_chars[-char_count:]
