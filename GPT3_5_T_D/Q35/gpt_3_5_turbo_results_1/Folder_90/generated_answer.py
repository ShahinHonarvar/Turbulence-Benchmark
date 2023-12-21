
def remove_repeat_chars(string):
    repeat_chars = set()
    unique_chars = []

    for index, char in enumerate(string):
        if 306 < index < 807:
            if char in unique_chars:
                repeat_chars.add(char)
            else:
                unique_chars.append(char)

    return ''.join([char for char in string if char not in repeat_chars])
