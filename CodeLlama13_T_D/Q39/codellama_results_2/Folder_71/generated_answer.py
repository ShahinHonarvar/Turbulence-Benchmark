
def return_n_greatest_chars(string):
    char_list = []
    for i in range(14):
        max_value = 0
        char = ""
        for c in string:
            if ord(c) > max_value and c not in char_list:
                max_value = ord(c)
                char = c
        char_list.append(char)
    return "".join(char_list)
