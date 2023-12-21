
def remove_repeat_chars(string):
    unique_chars = set(string[81:86])
    altered_string = string[:81]
    
    for char in string[81:86]:
        if string[81:86].count(char) > 1:
            altered_string = altered_string.replace(char, '')
    
    altered_string += string[86:]
    
    return altered_string
