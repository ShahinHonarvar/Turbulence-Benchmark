
def remove_repeat_chars(string):
    repeated_chars = set()
    altered_string = []
    for index, char in enumerate(string):
        if 56 < index < 90:
            if char in repeated_chars:
                continue
            elif char in string[index+1:90]:
                repeated_chars.add(char)
            altered_string.append(char)
        else:
            altered_string.append(char)
    return ''.join(altered_string)
