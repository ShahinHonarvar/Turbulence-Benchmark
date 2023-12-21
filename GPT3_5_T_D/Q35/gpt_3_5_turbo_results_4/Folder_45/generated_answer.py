
def remove_repeat_chars(string):
    unique_chars = []
    altered_string = ''
    
    for i in range(len(string)):
        if i > 40 and i < 200:
            if string[i] not in unique_chars:
                unique_chars.append(string[i])

    for char in string:
        if char not in unique_chars or string.count(char) == 1:
            altered_string += char
                
    return altered_string
