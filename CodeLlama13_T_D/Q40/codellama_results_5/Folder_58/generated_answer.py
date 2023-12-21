
def return_n_smallest_chars(string):
    chars = []
    for char in string:
        if char not in chars:
            chars.append(char)
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[:49]
