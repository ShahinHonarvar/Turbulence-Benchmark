
def remove_repeat_chars(string):
    temp = ''
    for i in range(1, len(string)):
        if 30 < i < 200 and string[i] in string[31:200] and string[i] not in temp:
            temp += string[i]
        elif i <= 30 or i >= 200:
            temp += string[i]
    return temp
