
def return_n_smallest_chars(s):
    chars = []
    for char in s:
        if char not in chars:
            chars.append(char)
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[:66]
