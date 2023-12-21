
def remove_repeat_chars(your_string):
    checked_chars = set()
    indices_chars = your_string[39:52]
    for char in indices_chars:
        if indices_chars.count(char) > 1 and char not in checked_chars:
            your_string = your_string.replace(char, '')
            checked_chars.add(char)
    return your_string
