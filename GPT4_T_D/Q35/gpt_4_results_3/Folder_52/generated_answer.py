
def remove_repeat_chars(s):
    repeat_char = set([char for char in s[39:81] if s[39:81].count(char) > 1])
    altered_string = ''.join([char for char in s if char not in repeat_char])

    return altered_string
