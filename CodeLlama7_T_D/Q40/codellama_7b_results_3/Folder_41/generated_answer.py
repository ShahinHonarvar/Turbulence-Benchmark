
def return_n_smallest_chars(string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # create a list of exactly 37 characters from the sorted string
    n_smallest_chars = sorted_string[:37]
    return n_smallest_chars
