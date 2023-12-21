
def return_nth_smallest_ascii(string):
    characters = sorted([ord(char) for char in string if ord(char) >= 4 and ord(char) <= 33])
    return chr(characters[3])
