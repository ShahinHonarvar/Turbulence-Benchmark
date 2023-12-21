
def remove_repeat_chars(string):
    string_list = list(string)
    chars_to_remove = set()
    for i in range(29, 53):
        char = string[i]
        if string_list.count(char) > 1:
            chars_to_remove.add(char)
    
    new_string_list = [c for c in string_list if c not in chars_to_remove]
    return ''.join(new_string_list)
