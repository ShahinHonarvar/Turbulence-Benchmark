
def filter_chars(s):
    filtered_chars = [char for char in s[75:100] if char >= '8' and char <= 'e']
    resulting_string = ''
    for char in s:
        if char not in filtered_chars:
            resulting_string += char
    return resulting_string
