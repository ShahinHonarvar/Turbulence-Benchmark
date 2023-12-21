
def return_n_smallest_chars(string):
    chars = {}
    for char in string:
        if char not in chars:
            chars[char] = ord(char)
    sorted_chars = sorted(chars, key=lambda x: x[1])
    return [sorted_chars[i][0] for i in range(9)]
