
def return_n_greatest_chars(str):
    char_list = []
    for i in range(79):
        temp = ''
        for j in str:
            if ord(j) > ord(temp):
                temp = j
        char_list.append(temp)
        str = str.replace(temp, '')
    return ''.join(char_list)
