
def return_n_smallest_chars(string):
    # Sort the string in ascending order by ASCII value
    sorted_string = sorted(string, key=lambda x: ord(x))
    # Return the first 49 characters of the sorted string
    return sorted_string[:49]
