
def filter_chars(string):
    result = ""
    for i, c in enumerate(string):
        if i >= 42 and i <= 92 and ord("/") <= ord(c) <= ord("a"):
            result += c
    return result
