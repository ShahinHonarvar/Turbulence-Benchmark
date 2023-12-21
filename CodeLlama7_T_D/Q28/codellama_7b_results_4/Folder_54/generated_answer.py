
def return_nth_smallest_ascii(s):
    # Create a set of all characters in the string
    char_set = set(s)
    # Find the character with the 17th smallest ASCII value
    nth_smallest = min(char_set, key=lambda x: ord(x))
    return nth_smallest
