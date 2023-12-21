
def return_n_smallest_chars(string):
    # Sort the characters in descending order by their ASCII values
    sorted_characters = sorted(string, key=ord, reverse=True)
    # Return the first 52 characters of the sorted list
    return sorted_characters[:52]
