
def remove_repeat_chars(s):
    string_section = s[101:200]
    repeated_chars = [char for char in string_section if string_section.count(char) > 1]
    return ''.join(char for char in s if char not in repeated_chars)
