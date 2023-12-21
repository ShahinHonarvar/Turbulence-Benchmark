
def filter_chars(my_str):
    selected_chars = [char for char in my_str[19:93] if '8' <= char <= 'm']
    for char in selected_chars:
        my_str = my_str.replace(char, '', 1)
    return my_str
