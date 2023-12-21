
def return_n_smallest_chars(string):
    chars = {}
    for char in string:
        if char not in chars:
            chars[char] = ord(char)
    sorted_chars = sorted(chars, key=chars.get, reverse=True)[:37]
    return sorted_chars
