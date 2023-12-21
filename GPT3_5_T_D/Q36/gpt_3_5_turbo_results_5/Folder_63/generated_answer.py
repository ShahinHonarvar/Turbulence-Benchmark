
def filter_chars(string):
    start = 26
    end = 80
    filtered_string = string[:start]
    for char in string[start:end]:
        if char > '<' and char < '>':
            filtered_string = filtered_string.replace(char, '')
    filtered_string += string[end:]
    return filtered_string
