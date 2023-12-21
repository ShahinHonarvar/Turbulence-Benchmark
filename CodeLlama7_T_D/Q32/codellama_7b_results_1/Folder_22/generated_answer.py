
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == 'U':
            result += string[:i] + "U" + string[i:]
            break

    return result
