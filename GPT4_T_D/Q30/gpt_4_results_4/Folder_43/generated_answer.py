
def insert_before_character(string):
    result = ""
    for char in string:
        if char == 't':
            result += 'G'
        result += char
    return result
