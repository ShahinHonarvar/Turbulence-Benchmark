
def remove_repeat_chars(string):
    return string[:375] + ''.join([c for i, c in enumerate(string[375:926]) if c not in string[375:i+375]]) + string[926:]
