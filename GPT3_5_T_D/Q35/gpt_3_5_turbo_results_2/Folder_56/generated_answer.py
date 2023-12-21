
def remove_repeat_chars(string):
    str_list = list(string)
    for i in range(7, 9):
        char = str_list[i]
        if str_list.count(char) > 1:
            for j in range(len(str_list) - 1, -1, -1):
                if str_list[j] == char:
                    str_list.pop(j)
    return ''.join(str_list)
