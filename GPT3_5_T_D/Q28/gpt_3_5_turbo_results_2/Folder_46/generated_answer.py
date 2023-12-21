
def return_nth_smallest_ascii(string):
    substring = string[34:86]
    characters = sorted(set(substring))
    nth_smallest = characters[19]
    return nth_smallest
