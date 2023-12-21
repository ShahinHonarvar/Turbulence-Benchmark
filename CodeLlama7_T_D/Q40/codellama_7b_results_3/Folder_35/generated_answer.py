
def return_n_smallest_chars(string):
    # sort the string in ascending order based on ASCII value
    sorted_string = sorted(string, key=lambda x: ord(x))
    # create a list of exactly 7 characters from the sorted string
    smallest_chars = sorted_string[:7]
    return smallest_chars
