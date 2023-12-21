
def return_nth_smallest_ascii(string):
    sub_string = string[1:67]
    characters = sorted([char for char in sub_string])
    return characters[7]
