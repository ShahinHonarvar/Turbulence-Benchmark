
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if 19 <= i <= 33 and c >= "S" and c <= "{":
            continue
        result += c
    return result
