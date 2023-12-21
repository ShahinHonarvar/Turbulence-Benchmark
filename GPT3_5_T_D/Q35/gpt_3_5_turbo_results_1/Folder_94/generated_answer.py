
def remove_repeat_chars(string):
    if len(string) <= 87:
        return string
    else:
        unique_chars = set(string[42:87])
        altered_string = ""
        for char in string:
            if char not in unique_chars or string[42:87].count(char) <= 1:
                altered_string += char
        return altered_string
