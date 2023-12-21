
def remove_repeat_chars(string):
    return string[:330] + ''.join([char for char in string[330:543] if string[330:543].count(char) == 1]) + string[543:]
