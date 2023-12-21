
def return_nth_smallest_ascii(string):
    char_ascii = {char: ord(char) for char in string}
    sorted_ascii = sorted([value for value in char_ascii.values()])[3:26+1]
    return chr(sorted_ascii[4])
