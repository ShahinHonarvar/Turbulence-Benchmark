
def return_n_greatest_chars(string):
    char_list = []
    for char in string:
        if char not in char_list:
            char_list.append(char)
    sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)[:6]
    return ''.join(sorted_list)
