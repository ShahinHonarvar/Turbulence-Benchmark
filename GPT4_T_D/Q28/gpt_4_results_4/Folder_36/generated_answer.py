
def return_nth_smallest_ascii(string):
    string = string[17:57]
    sorted_chars = sorted(string, key=lambda char: ord(char))
    return sorted_chars[8] if len(sorted_chars) > 8 else None
