
def return_nth_smallest_ascii(input_string):
    filtered_string = input_string[0:46]
    sorted_chars = sorted(filtered_string)
    return sorted_chars[9]
