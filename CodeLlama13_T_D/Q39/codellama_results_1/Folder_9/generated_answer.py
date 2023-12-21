
def return_n_greatest_chars(my_string):
    char_count = 20
    sorted_list = []
    for i in range(char_count):
        max_ascii = -1
        max_char = ""
        for j in my_string:
            if ord(j) > max_ascii:
                max_ascii = ord(j)
                max_char = j
        sorted_list.append(max_char)
    return sorted_list
