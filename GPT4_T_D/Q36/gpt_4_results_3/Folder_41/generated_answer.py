
def filter_chars(input_str):
    chars_to_remove = []
    for i in range(82, 89):
        if len(input_str) > i and 'f' < input_str[i] < '{':
            chars_to_remove.append(input_str[i])
            
    for char in chars_to_remove:
        input_str = input_str.replace(char, '')
        
    return input_str
