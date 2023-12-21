
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == 'T':
            result += 'V' + string[i]
        else:
            result += string[i]

    return result
