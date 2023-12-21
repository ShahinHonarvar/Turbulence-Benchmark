
def filter_chars(input_str):
    substring = input_str[324:526]
    
    for ch in substring:
        if ')' < ch < 'O':
            input_str = input_str.replace(ch, '')

    return input_str
