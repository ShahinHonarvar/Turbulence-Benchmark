
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 46 <= ord(char) <= 85 and char >= "-" and char <= "X":
            continue
        else:
            result += char
    return result
