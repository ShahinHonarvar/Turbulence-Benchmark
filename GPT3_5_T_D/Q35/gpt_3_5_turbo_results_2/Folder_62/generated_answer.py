
def remove_repeat_chars(string):
    unique_chars = []
    altered_string = ''
    
    for char in string:
        if 50 <= string.index(char) < 92 and char not in unique_chars:
            unique_chars.append(char)
        
        if 50 <= string.index(char) < 92 and string.count(char) == 1:
            altered_string += char
    
    return altered_string
