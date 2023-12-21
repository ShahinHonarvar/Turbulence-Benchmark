
def return_nth_smallest_ascii(s):
    chars = list(set(s))
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    nth_smallest = sorted_chars[9:22]
    return nth_smallest[3]
