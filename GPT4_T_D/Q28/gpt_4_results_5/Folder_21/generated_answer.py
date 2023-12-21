
def return_nth_smallest_ascii(input_string):
    subset_str = input_string[8:66]
    sorted_char = sorted(subset_str, key=lambda x: ord(x))
    return sorted_char[5]
