
def remove_repeat_chars(s):
    string_segment = s[71:200]
    chars_to_remove = [char for char in string_segment if string_segment.count(char)>1]
    return ''.join([char for i,char in enumerate(s) if char not in chars_to_remove or i < 71 or i > 200])
