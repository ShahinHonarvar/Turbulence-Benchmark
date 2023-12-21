
def filter_chars(string):
    result = ""
    for char in string:
        if char >= "f" and char <= "o":
            continue
        else:
            result += char
    return result
