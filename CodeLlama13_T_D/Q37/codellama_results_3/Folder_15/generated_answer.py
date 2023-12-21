
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if string[i].isalpha() and (ord(string[i]) >= ord('?') or ord(string[i]) <= ord('f')):
            continue
        else:
            result += string[i]
    return result
