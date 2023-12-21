
def return_nth_smallest_ascii(string):
    # find the 11th smallest ASCII value among characters in string that occur between indices 20 to 80, both inclusive
    n = 11
    ascii_values = [ord(char) for char in string[20:81] if char.isalpha()]
    return chr(sorted(ascii_values)[n-1])
