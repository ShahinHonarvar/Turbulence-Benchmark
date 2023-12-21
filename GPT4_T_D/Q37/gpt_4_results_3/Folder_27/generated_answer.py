
def filter_chars(s):
    between_indices = s[43:81]
    to_remove = [char for char in between_indices if '=' <= char <= 'E']
    return ''.join([char for char in s if char not in to_remove])
