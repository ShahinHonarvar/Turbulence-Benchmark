
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 13 <= i < 40 and ":" < char < "C":
            result += char
        else:
            result += char
    return result
