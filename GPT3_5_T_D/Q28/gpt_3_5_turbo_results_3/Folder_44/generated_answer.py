
def return_nth_smallest_ascii(string):
    substring = string[20:31]
    chars = list(set(substring))
    chars.sort(key = lambda x: ord(x))
    return chars[7]
