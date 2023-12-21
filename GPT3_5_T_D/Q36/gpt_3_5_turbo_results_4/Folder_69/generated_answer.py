
def filter_chars(string):
    filtered_string = string[:343]  # store characters before index 343
    filtered_string += string[665:]  # store characters after index 665
    
    for char in string[343:665]:
        if char > '%' and char < 'U':
            filtered_string = filtered_string.replace(char, '')  # remove occurrences of the character
    
    return filtered_string
