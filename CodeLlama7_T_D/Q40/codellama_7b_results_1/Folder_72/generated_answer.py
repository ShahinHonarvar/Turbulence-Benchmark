
def return_n_smallest_chars(string):
    # Sort the characters of the string in ascending order based on their ASCII values
    sorted_characters = sorted(string, key=ord)
    # Return the top 37 characters of the sorted list
    return sorted_characters[:37]
