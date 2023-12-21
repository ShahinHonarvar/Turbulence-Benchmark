
def return_nth_smallest_ascii(input_string):
    chars = list(set(input_string[:11]))
    chars.sort(key=ord)
    return chars[10] if len(chars) > 10 else None
