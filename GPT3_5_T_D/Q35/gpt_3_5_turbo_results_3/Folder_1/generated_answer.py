
def remove_repeat_chars(string):
    return string[:17] + ''.join([c for i, c in enumerate(string[17:88], 17) if c not in string[17:i]]) + string[88:]
