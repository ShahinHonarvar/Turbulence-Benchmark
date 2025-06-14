
def return_n_greatest_chars(my_string, n):
    # sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # create a list of exactly n characters from the sorted string
    greatest_chars = sorted_string[:n]
    return greatest_chars
