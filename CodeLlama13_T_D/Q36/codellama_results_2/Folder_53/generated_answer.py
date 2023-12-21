
def filter_chars(s):
    chars = list(s)
    for i in range(90, 97):
        if ord(chars[i]) > ord('j') and ord(chars[i]) < ord('w'):
            chars.remove(chars[i])
    return ''.join(chars)
