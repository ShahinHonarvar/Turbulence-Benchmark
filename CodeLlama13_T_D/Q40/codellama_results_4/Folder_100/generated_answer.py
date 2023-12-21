
def return_n_smallest_chars(string):
    char_list = []
    for i in range(72):
        min_char = string[0]
        for j in range(1, len(string)):
            if ord(string[j]) < ord(min_char):
                min_char = string[j]
        char_list.append(min_char)
        string = string.replace(min_char, "")
    return sorted(char_list, reverse=True)
