
def return_nth_smallest_ascii(input_string):
    return sorted([ord(char) for char in input_string[0:13]])[12]
