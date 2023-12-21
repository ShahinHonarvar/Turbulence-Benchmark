
def insert_after_character(string, character):
    result = ''
    for i in range(len(string)):
        if string[i] == character:
            result += string[i] + 'n'
        else:
            result += string[i]
    return result
