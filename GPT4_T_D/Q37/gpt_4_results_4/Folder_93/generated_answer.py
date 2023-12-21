
def filter_chars(my_string):
    picked_chars = [char for char in my_string[38:70] if char >= 'H' and char <= 'e']
    return ''.join(char for char in my_string if char not in picked_chars)
