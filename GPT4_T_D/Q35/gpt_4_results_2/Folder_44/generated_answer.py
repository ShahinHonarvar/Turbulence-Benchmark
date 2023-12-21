
def remove_repeat_chars(s):
    sub_str = s[37:52]
    chars_to_remove = set([char for char in sub_str if sub_str.count(char) > 1])

    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
            
    return ''.join(result)
