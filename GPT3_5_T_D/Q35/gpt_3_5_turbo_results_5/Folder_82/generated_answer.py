
def remove_repeat_chars(text):
    for index in range(30, 200):
        char = text[index]
        if text.count(char) > 1:
            text = text.replace(char, '')
    return text
