
def return_n_smallest_chars(string):
    char_list = []
    for i in string:
        if len(char_list) < 60 and ord(i) not in char_list:
            char_list.append(ord(i))
    char_list.sort()
    return [chr(i) for i in char_list]
