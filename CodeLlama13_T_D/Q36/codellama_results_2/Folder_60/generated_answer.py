
def filter_chars(s):
    result = ""
    for i in range(23, 83):
        if s[i] > "f" and s[i] < "o":
            result += s[i]
    return result
