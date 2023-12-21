
def remove_repeat_chars(s):
    unique_chars = set(s[78:84])
    repeat_chars = {char for char in unique_chars if s[78:84].count(char) > 1}
    altered_string = "".join(char for char in s if char not in repeat_chars)
    return altered_string
