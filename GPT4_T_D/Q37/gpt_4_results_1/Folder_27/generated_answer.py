
def filter_chars(s):
    selected_chars = [char for char in s[43:81] if '=' <= char <= 'E']
    return ''.join([char for char in s if char not in selected_chars])
