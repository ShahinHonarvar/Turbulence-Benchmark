
def return_n_smallest_chars(my_string):
    # Sort the characters in ascending order based on their ASCII values
    sorted_chars = sorted(my_string, key=ord)
    # Create a list of exactly 87 characters of the given string that have the smallest ASCII values
    smallest_chars = sorted_chars[:87]
    # Sort the list in descending order
    smallest_chars.sort(reverse=True)
    return smallest_chars
