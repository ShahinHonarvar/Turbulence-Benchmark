
def remove_repeat_chars(string):
    index_16 = 16
    index_87 = 87
    altered_string = ""
    for i in range(len(string)):
        if i >= index_16 and i < index_87:
            if string.count(string[i]) == 1 or i < string.index(string[i], index_16, index_87):
                altered_string += string[i]
        else:
            altered_string += string[i]
    return altered_string
