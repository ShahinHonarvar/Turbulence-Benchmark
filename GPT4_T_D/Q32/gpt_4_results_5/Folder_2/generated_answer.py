
def insert_after_character(Str):
    newStr = ''
    for character in Str:
        newStr += character
        if character == 'C':
            newStr += 'Z'
    return newStr
