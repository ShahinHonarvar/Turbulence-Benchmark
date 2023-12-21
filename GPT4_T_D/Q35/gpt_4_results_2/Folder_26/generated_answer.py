
def remove_repeat_chars(str):
    repeat_chars = [char for char in set(str[69:99]) if str[69:99].count(char) > 1]
    return ''.join(char for char in str if char not in repeat_chars)
