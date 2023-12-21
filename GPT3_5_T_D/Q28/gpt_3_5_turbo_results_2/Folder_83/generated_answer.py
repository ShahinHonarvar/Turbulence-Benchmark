
def return_nth_smallest_ascii(string):
    chars = [char for char in string[30:71] if char in string[:30]]
    sorted_chars = sorted(chars)
    return sorted_chars[14]
