
def remove_repeat_chars(string):
    start_index = 29
    end_index = 53
    repeat_chars = set()
    for char in string[start_index:end_index]:
        if string.count(char) > 1:
            repeat_chars.add(char)
    
    new_string = ""
    for char in string:
        if char not in repeat_chars:
            new_string += char
    return new_string
