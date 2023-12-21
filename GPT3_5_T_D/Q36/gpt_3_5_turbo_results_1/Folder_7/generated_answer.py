
def filter_chars(string):
    filtered_string = string[:502]
    filtered_string += string[502:946].replace('x', '').replace('X', '')
    filtered_string += string[946:]
    return filtered_string
