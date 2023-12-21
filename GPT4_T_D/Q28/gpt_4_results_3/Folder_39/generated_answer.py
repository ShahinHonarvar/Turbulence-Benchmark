
def return_nth_smallest_ascii(string):
    string = string[1:67]
    sorted_characters = sorted(string, key=lambda character: ord(character))
    return sorted_characters[7]
