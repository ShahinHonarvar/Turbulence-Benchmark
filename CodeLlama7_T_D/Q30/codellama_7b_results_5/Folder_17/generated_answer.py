
def insert_before_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == 'Q':
            result += 'I'

        result += string[i]

    return result
