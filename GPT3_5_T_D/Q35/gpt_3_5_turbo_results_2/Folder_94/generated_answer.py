
def remove_repeat_chars(string):
    repeated_chars = set()
    altered_string = ""

    for index, char in enumerate(string):
        if 42 < index < 87:
            if char not in repeated_chars and char in string[index+1:87]:
                repeated_chars.add(char)
            if char not in repeated_chars:
                altered_string += char

    return altered_string
