
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string if ord(char) <= 69 and ord(char) >= 0]
    return chr(sorted(ascii_values)[9])
