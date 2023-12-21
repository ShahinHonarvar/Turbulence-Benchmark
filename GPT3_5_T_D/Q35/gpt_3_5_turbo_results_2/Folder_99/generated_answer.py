
def remove_repeat_chars(string):
    return string[:450] + ''.join(c for i, c in enumerate(string[450:905]) if c not in string[450:905][:i]) + string[905:]
