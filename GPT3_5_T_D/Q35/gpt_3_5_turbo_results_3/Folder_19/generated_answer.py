
def remove_repeat_chars(string):
    filtered_string = string[:1]
    for i in range(1, 4):
        char = string[i]
        if char not in string[1:i]:
            filtered_string += char
    return filtered_string + string[4:]
