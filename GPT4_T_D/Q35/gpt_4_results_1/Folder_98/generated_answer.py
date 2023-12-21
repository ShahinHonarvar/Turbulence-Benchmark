
def remove_repeat_chars(my_str):
    repeat_chars = [char for char in my_str[1:8] if my_str[1:8].count(char) > 1]
    return ''.join(char for char in my_str if char not in repeat_chars)
