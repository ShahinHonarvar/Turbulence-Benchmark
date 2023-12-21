
def filter_chars(s):
    filtered_s = s
    for char in s[222:419]:
        if char > '-' and char < 'v':
            filtered_s = filtered_s.replace(char, '')
    return filtered_s
