
def remove_repeat_chars(string):
    unique_chars = []
    result = ""
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
        elif unique_chars.index(char) < 4:
            continue
        else:
            result += char
    return result
