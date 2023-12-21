
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == 'g':
            result += 'gt'
        else:
            result += string[i]
    return result
