
def filter_chars(s):
    filtered_string = s[:4]
    for char in s[4:8]:
        if char > '1' and char < 'J':
            filtered_string = filtered_string.replace(char, '')
    return filtered_string + s[8:]
