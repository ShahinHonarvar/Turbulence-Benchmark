
def filter_chars(string):
    filtered_chars = [char for char in string[52:82] if 'A'<=char<='U']
    new_string = ''.join([char for char in string if char not in filtered_chars])
    return new_string
