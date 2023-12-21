
def remove_repeat_chars(string):
    return string[:50] + ''.join([c for c in string[50:76] if string[50:76].count(c)==1]) + string[76:]
