
def remove_repeat_chars(string):
    return "".join(char for i, char in enumerate(string) if 125 < i < 825 or char not in string[125:825])
