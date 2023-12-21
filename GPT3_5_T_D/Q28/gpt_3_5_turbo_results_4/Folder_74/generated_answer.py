
def return_nth_smallest_ascii(string):
    characters = string[1:32]
    sorted_characters = sorted(characters)
    nth_smallest = sorted_characters[5]
    return nth_smallest
