
def remove_repeat_chars(string):
    return string[:409] + ''.join([char for char in string[409:502] if string[409:502].count(char) == 1]) + string[502:]
