
def remove_repeat_chars(str):
    more_than_once = [char for char in str[74:84] if str[74:84].count(char) > 1]
    return ''.join(char for char in str if char not in more_than_once)
