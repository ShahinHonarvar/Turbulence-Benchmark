
def remove_repeat_chars(str_val):
    repeat_chars = [char for char in str_val[1:3] if str_val[1:3].count(char) > 1]
    return ''.join(char for char in str_val if char not in repeat_chars)
