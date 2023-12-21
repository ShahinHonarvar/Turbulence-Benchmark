
def filter_chars(s):
    result = ""
    for i, c in enumerate(s):
        if 221 <= ord(c) < 419 and c > "-" and c < "v":
            result += c
    return result
