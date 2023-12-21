
def insert_after_character(s):
    output = ""
    for char in s:
        output += char
        if char == 'r':
            output += 'w'
    return output
