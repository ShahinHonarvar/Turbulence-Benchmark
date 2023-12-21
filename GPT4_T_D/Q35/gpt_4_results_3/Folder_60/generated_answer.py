
def remove_repeat_chars(s):
    sub_str = s[39:52]
    characters_to_remove = [char for char in sub_str if sub_str.count(char) > 1]
    return ''.join([char for char in s if char not in characters_to_remove])
