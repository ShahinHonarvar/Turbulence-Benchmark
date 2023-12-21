
def return_nth_smallest_ascii(string):
    chars = string[21:60]
    chars = list(filter(lambda x: x in string, chars))
    chars.sort(key=lambda x: ord(x))
    return chars[10]
