
def remove_repeat_chars(s):
    substring = s[7:9]
    char_list = [char for char in substring if substring.count(char) > 1]
    new_string = ''.join([char for char in s if char not in char_list])
    return new_string
