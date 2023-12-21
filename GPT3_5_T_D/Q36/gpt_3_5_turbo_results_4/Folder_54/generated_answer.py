
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 18 and i < 38:
            if char > ')' and char < 'P':
                continue
        filtered_string += char
    return filtered_string
