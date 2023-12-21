
def remove_repeat_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 50 or i >= 200 or string[i:200].count(char) <= 1])
