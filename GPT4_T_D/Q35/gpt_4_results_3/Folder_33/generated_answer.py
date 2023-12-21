
def remove_repeat_chars(string):
    if len(string) < 826:
        return string
    else:
        repeat_chars = [char for char in string[126:825] if string[126:825].count(char) > 1]
        return ''.join([char for char in string if char not in repeat_chars])
