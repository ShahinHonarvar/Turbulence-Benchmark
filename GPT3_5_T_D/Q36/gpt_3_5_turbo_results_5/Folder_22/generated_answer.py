
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index < 55 or index >= 84 or ord(char) <= ord(';') or ord(char) >= ord('z'):
            filtered_string += char
    
    return filtered_string
