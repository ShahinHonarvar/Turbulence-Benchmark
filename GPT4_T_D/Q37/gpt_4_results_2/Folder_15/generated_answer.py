
def filter_chars(s):
    filter_list = [c for c in s[2:7] if '?' <= c <= 'f']
    filtered_string = ''
    for char in s:
        if char not in filter_list:
            filtered_string += char
    return filtered_string
