
def filter_chars(string):
    start_index = 1
    end_index = 6
    filtered_string = string[:start_index]
    for char in string[start_index:end_index]:
        if char > ',' and char < 'f':
            filtered_string += string[start_index:end_index].replace(char, '')
        else:
            filtered_string += char
    filtered_string += string[end_index:]
    return filtered_string
