
def remove_repeat_chars(string):
    return string[:306] + ''.join([char for char in string[306:807] if string[306:807].count(char) == 1]) + string[807:]
