
def remove_repeat_chars(string):
    if len(string) < 7 or len(string) < 9:
        return string
    else:
        chars_to_remove = []
        for char in string[7:9]:
            if string.count(char) > 1:
                chars_to_remove.append(char)
        
        altered_string = ""
        for char in string:
            if char not in chars_to_remove:
                altered_string += char
        
        return altered_string
