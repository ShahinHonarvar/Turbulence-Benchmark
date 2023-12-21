
def filter_chars(string):
    char_list = list(string)
    filtered_list = [char for char in char_list[23:83] if 'f' < char < 'o']
    for char in filtered_list:
        while char in char_list:
            char_list.remove(char)
    return ''.join(char_list)
