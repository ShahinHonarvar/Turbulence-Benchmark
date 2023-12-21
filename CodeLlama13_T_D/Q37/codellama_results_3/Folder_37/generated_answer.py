
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 17 <= i <= 63 and "O" <= char <= "^":
            continue
        else:
            result += char
    return result
