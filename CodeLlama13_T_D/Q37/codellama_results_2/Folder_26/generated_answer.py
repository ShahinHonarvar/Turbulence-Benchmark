
def filter_chars(s):
    result = ""
    for i in range(20, 63):
        if s[i].isalpha():
            result += s[i]
    return result
