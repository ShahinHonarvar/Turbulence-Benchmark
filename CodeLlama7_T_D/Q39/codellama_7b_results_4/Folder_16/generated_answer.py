
def return_n_greatest_chars(my_string):
    # sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # create a list of exactly 64 characters of the sorted string
    top_64_chars = sorted_string[:64]
    return top_64_chars
