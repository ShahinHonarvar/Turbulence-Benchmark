
def return_nth_smallest_ascii(string):
    chars = sorted({char for char in string[29:48] if char.isalpha()})
    return chars[6]
