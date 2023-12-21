
def filter_chars(string):
    result = ""
    for i, char in enumerate(string[30:51]):
        if ord(char) > ord('/') and ord(char) < ord('J'):
            result += string[:i+1] + string[i+2:]
    return result
