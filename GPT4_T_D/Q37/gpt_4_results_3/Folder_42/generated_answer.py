
def filter_chars(s):
    char_list = list(s[73:75])
    filtered_chars = [char for char in char_list if char >= 'U' and char <= 'l']
    result_str = ''
    for char in s:
        if char not in filtered_chars:
            result_str += char
    return result_str
