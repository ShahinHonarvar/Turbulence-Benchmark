
def filter_chars(input_str):
    relevant_chars = set(input_str[40:87])
    relevant_chars = [char for char in relevant_chars if '!'<char<'{']
    for char in relevant_chars:
        input_str = input_str.replace(char, '')
    return input_str
