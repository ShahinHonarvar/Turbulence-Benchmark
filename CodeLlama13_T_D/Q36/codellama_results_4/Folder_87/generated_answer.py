
def filter_chars(string):
    new_str = ''
    for i in range(len(string)):
        if string[i].isalnum() and (ord(string[i]) > 32 and ord(string[i]) < 61):
            new_str += string[i]
    return new_str
