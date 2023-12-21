
def remove_repeat_chars(string):
    new_string = ""
    for i in range(len(string)):
        if 77 < i < 84:
            if string[i] not in string[77:i]:
                new_string += string[i]
        else:
            new_string += string[i]
    return new_string
