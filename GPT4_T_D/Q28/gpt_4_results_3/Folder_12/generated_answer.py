
def return_nth_smallest_ascii(input_string):
    selected_chars = sorted(list(input_string[3:27]))
    return sorted(selected_chars, key=lambda x:ord(x))[4]
