
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == 'P':
            result += string[i] + 'V'
        else:
            result += string[i]
    return result
