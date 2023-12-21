
def return_n_smallest_chars(s):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(s, key=ord)
    # return the first 21 characters of the sorted string
    return sorted_string[:21]
