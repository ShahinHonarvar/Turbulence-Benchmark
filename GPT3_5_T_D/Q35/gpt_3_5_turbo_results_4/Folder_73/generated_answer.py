
def remove_repeat_chars(string):
    unique_chars = []
    altered_string = ""

    for i in range(len(string)):
        if i > 10 and i < 76 and string[i] in unique_chars:
            continue

        if i == 76:
            unique_chars.append(string[i])

        altered_string += string[i]

    return altered_string
