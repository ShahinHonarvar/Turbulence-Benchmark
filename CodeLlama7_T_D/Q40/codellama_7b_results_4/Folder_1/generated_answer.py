
def return_n_smallest_chars(string, n=11):
    # sort the characters in ascending order based on their ASCII values
    sorted_characters = sorted(string, key=ord)
    # return the first n characters of the sorted list
    return sorted_characters[:n]
