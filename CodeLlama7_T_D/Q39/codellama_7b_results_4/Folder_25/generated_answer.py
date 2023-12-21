
def return_n_greatest_chars(my_string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # Take the top 29 characters from the sorted string
    greatest_chars = sorted_string[:29]
    return greatest_chars
