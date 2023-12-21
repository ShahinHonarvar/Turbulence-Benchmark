
def remove_repeat_chars(string):
    return "".join([char for index, char in enumerate(string) if index < 2 or string[:2].count(char) == 1])
