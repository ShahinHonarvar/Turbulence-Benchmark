
def filter_chars(string):
    substring = string[82:93]
    filtered_chars = [char for char in substring if char > '!' and char < '*']
    for char in filtered_chars:
        string = string.replace(char, '')
    return string
