
def return_nth_smallest_ascii(string):
    # create a list of ASCII values for each character in the string
    ascii_values = [ord(c) for c in string]

    # sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)

    # return the 16th smallest ASCII value among those characters that occur between indices 5 to 82, both inclusive
    return chr(sorted_ascii_values[5 + 16 - 1])
