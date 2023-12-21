
def insert_before_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == '5':
            result += 'R' + string[i]
        else:
            result += string[i]
    return result
