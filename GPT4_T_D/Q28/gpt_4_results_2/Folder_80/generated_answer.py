
def return_nth_smallest_ascii(input_string):
    substring = input_string[51:90]
    sorted_chars = sorted(substring, key=ord)
    if len(sorted_chars) < 14:
        return None
    else:
        return sorted_chars[13]
