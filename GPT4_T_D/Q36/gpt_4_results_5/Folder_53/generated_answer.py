
def filter_chars(s):
    filtered_chars = [char for char in s[91:97] if char > 'j' and char < 'w']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
