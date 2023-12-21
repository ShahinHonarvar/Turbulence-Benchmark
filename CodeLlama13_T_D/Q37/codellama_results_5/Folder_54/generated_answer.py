
def filter_chars(string):
    result = ""
    for i in range(46, 85+1):
        if string[i].isalnum():
            result += string[i]
    return result
