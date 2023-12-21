
def remove_repeat_chars(string):
    return string[:375] + ''.join(char for char in string[375:926] if string[375:926].count(char) <= 1) + string[926:]
