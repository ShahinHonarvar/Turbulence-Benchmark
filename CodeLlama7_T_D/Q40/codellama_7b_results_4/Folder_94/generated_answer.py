
def return_n_smallest_chars(string):
    # Sort the string in descending order based on ASCII value
    sorted_string = sorted(string, key=ord, reverse=True)
    # Return the first 87 characters of the sorted string
    return sorted_string[:87]
