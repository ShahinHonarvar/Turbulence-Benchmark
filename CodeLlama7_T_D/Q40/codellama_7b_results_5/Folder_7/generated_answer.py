
def return_n_smallest_chars(string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # create a list of exactly 49 characters from the sorted string
    smallest_characters = sorted_string[:49]
    return smallest_characters
