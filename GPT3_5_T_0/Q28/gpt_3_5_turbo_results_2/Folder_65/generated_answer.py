
def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string[32:68] if char in string]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[11]
