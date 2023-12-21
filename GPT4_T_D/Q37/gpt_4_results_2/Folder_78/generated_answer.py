
def filter_chars(input_str):
    filtered_str = ""
    for i, char in enumerate(input_str):
        if 75 <= i <= 99 and '8' <= char <= 'e':
            input_str = input_str.replace(char, "")
        else:
            filtered_str += char
    return input_str
