
def return_nth_smallest_ascii(string):
    sub_string = string[25:46]
    unique_chars = []
    for char in sub_string:
        if char not in unique_chars:
            unique_chars.append(char)
    sorted_chars = sorted(unique_chars)
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]
