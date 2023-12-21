
def return_nth_smallest_ascii(string):
    filtered_string = string[32:68]
    sorted_chars = sorted(filtered_string, key=lambda char: ord(char))
    return sorted_chars[11]
