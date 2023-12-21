
def remove_repeat_chars(input_string):
    window = set(input_string[14:70])
    result = []

    for i, char in enumerate(input_string):
        if (char in window) and (i > 13) and (i < 70):
            if input_string.count(char) > 1:
                window.remove(char)
        else:
            result.append(char)
    return ''.join(result)
