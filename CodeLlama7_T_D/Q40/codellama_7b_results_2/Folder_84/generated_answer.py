
def return_n_smallest_chars(my_string):
    # sort the string in ascending order based on ASCII value
    sorted_string = sorted(my_string, key=lambda x: ord(x))
    # create a list of exactly 10 characters from the sorted string
    smallest_chars = sorted_string[:10]
    return smallest_chars
