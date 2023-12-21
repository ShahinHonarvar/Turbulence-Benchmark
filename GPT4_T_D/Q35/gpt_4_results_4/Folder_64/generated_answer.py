
def remove_repeat_chars(my_string):
    repeat_chars = [char for char in my_string[1:5] if my_string[1:5].count(char) > 1]
    return ''.join(char for char in my_string if char not in repeat_chars)
