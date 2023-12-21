
def filter_chars(input_str):
    for char_index in range(36, 60):
        if len(input_str) > char_index:
            char = input_str[char_index]
            if '!' < char < 'B':
                input_str = input_str.replace(char, "")

    return input_str
