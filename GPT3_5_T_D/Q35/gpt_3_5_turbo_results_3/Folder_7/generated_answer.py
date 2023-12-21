
def remove_repeat_chars(string):
    return string[:375] + ''.join(c for c in string[375:926] if string[375:926].count(c) == 1) + string[926:]
