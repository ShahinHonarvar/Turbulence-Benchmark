
def remove_repeat_chars(string):
    unique_chars = set(string)
    for char in unique_chars:
        if string.count(char) > 1:
            indices = [i for i, c in enumerate(string) if c == char]
            if 100 < indices[0] < 200:
                string = string.replace(char, "")
    return string
