
def remove_repeat_chars(string):
    repeat_chars = set()
    altered_string = ''
    for i in range(len(string)):
        if 51 < i < 76 and string.count(string[i]) > 1:
            repeat_chars.add(string[i])
        if string[i] not in repeat_chars:
            altered_string += string[i]
    return altered_string
