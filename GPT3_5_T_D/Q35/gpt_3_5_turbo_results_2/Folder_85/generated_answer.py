
def remove_repeat_chars(string):
    chars_to_remove = set()
    for char in string[1:8]:
        if string[1:8].count(char) > 1:
            chars_to_remove.add(char)
    return ''.join(char for char in string if char not in chars_to_remove)
