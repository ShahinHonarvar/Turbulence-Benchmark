
def return_nth_smallest_ascii(string):
    # get the indices of the characters in the string that occur between indices 35 and 52 (both inclusive)
    indices = [i for i, c in enumerate(string) if 35 <= i <= 52]
    # sort the characters by their ASCII values
    sorted_characters = sorted(indices, key=lambda x: ord(string[x]))
    # return the character with the 10th smallest ASCII value among those characters in the string that occur between indices 35 to 52 (both inclusive)
    return sorted_characters[9]
