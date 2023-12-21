
def return_nth_smallest_ascii(string):
    return min([ord(char) for char in string[0:6]]) + 7
