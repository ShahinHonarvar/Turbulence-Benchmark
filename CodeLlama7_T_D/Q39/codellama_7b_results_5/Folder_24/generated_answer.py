
def return_n_greatest_chars(string, n):
    char_list = []
    for char in string:
        char_list.append((ord(char), char)))
    char_list.sort(key=lambda x: (-x[0], x[1])))
    return [x[1] for x in char_list[:n]]
