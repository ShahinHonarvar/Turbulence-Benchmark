
def remove_repeat_chars(string):
    return ''.join([char for idx, char in enumerate(string) if idx < 90 or idx >= 200 or string[90:200].count(char) <= 1])
