
def return_nth_smallest_ascii(string):
    ascii_list = [ord(char) for char in string[38:83] if char in string]
    sorted_list = sorted(ascii_list)
    return chr(sorted_list[19])
