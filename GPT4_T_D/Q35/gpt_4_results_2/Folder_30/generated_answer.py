
def remove_repeat_chars(my_string):
    
    substring = my_string[23:24]
    unique_chars = set(substring)
    
    for char in unique_chars:
        if substring.count(char) > 1:
            my_string = my_string.replace(char, '')
    
    return my_string
