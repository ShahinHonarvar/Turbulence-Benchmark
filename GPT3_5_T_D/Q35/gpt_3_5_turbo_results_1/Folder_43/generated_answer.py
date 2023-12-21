
def remove_repeat_chars(string):
    remove_chars = []
    for char in string[10:28]:
        if string[10:28].count(char) > 1:
            remove_chars.append(char)
    return ''.join([c for c in string if c not in remove_chars])
