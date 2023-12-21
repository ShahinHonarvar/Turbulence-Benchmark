
def return_nth_smallest_ascii(input_string):
    substring = input_string[5:48]
    sorted_ascii = sorted([char for char in substring], key=ord)
    return sorted_ascii[12]
