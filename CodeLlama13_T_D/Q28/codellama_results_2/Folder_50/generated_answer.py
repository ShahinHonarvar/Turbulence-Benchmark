
def return_nth_smallest_ascii(string):
    char_list = []
    for i in range(25, 89):
        if string[i].isalpha():
            char_list.append((ord(string[i]), string[i]))
    return sorted(char_list)[10][1]
