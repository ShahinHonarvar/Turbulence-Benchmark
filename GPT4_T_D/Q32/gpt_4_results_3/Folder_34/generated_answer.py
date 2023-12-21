
def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'A':
            result += 'Aa'
        else:
            result += char
    return result
