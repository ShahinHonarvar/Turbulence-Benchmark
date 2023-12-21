
def filter_chars(my_str):
    to_remove = [char for char in my_str[36:80] if 'a' <= char <= 'i']
    return ''.join(char for char in my_str if char not in to_remove)
