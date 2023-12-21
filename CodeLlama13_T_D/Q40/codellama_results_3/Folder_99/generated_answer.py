
def return_n_smallest_chars(string):
    char_list = []
    for i in range(35):
        min_char = ''
        for j in range(len(string)):
            if string[j] not in char_list:
                if min_char == '':
                    min_char = string[j]
                elif ord(min_char) > ord(string[j]):
                    min_char = string[j]
        char_list.append(min_char)
    return sorted(char_list, reverse=True)
