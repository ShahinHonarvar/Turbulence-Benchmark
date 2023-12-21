
def return_nth_smallest_ascii(string):
    filtered_chars = [char for char in string[33:86] if char.isalpha()]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[12]
