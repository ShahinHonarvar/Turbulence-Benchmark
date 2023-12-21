
def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if i < 69 or i > 87:
            result += c
        elif ord(c) > ord('#') and ord(c) < ord('L'):
            continue
        else:
            result += c
    return result
