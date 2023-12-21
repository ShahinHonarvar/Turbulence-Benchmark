
def remove_repeat_chars(string):
    repeated_chars = set()
    for char in string[72:93]:
        if string[72:93].count(char) > 1:
            repeated_chars.add(char)
    string_list = list(string)
    for char in repeated_chars:
        string_list = [c for c in string_list if c != char]
    return ''.join(string_list)
