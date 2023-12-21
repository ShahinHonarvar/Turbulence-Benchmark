
def return_nth_smallest_ascii(s):
    # create a list of ASCII values for each character in the string
    ascii_values = [ord(c) for c in s]
    # filter out characters that are not between indices 14 to 66, both inclusive
    filtered_values = [v for v in ascii_values if 14 <= v <= 66]
    # sort the filtered values in ascending order
    sorted_values = sorted(filtered_values)
    # return the 8th smallest ASCII value in the sorted list
    return sorted_values[7]
