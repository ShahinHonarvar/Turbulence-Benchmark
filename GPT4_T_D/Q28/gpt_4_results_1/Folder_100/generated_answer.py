
def return_nth_smallest_ascii(input_string):
    selected_chars = [char for char in input_string[5:48]]
    sorted_chars = sorted(selected_chars, key=lambda char: ord(char))
    return sorted_chars[12]
