
def remove_repeat_chars(string):
    ignore_indices = set()
    for index in range(56, 88):
        if string[index] in string[index + 1: 88]:
            ignore_indices.add(index)
    new_string = ''
    for index, char in enumerate(string):
        if index not in ignore_indices:
            new_string += char
    return new_string
