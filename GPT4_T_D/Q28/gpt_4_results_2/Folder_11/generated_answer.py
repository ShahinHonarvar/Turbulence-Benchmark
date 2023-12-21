
def return_nth_smallest_ascii(string):
    sub_string = string[9:60]
    sorted_chars = sorted(sub_string, key=ord)
    return sorted_chars[5] if len(sorted_chars) > 5 else 'Not enough characters'
