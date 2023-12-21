
def remove_repeat_chars(input_str):
    relevant_chars = input_str[104:802]
    for char in set(relevant_chars):
        if relevant_chars.count(char) > 1:
            input_str = input_str.replace(char, '')
    return input_str
