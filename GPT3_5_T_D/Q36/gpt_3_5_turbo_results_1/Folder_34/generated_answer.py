
def filter_chars(string):
    char_list = list(string)
    for i in range(10, 79):
        if ord(char_list[i]) > ord('?') and ord(char_list[i]) < ord('m'):
            char_list = [char for char in char_list if char != char_list[i]]
    
    return "".join(char_list)
