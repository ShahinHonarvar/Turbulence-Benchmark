
def filter_chars(str_arg):
    chars_to_remove = [char for char in str_arg[19:95] if 'K' < char < 'a']
    str_arg = ''.join([char for char in str_arg if char not in chars_to_remove])
    return str_arg
