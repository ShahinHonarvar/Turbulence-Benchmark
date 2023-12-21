
def return_nth_smallest_ascii(input_string):
    relevant_chars = input_string[62:84]
    sorted_chars = sorted(relevant_chars, key=lambda x: ord(x))
    return sorted_chars[8]
