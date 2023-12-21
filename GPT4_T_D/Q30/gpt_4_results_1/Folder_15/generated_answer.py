
def insert_before_character(string):
    result = ""
    for character in string:
        if character == 'o':
            result += 'o'
        result += character
    return result
