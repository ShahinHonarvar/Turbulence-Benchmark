
def remove_repeat_chars(my_string):
    repeat_chars = set([char for char in my_string[376:926] if my_string[376:926].count(char) > 1])
    return ''.join(char for char in my_string if char not in repeat_chars)
