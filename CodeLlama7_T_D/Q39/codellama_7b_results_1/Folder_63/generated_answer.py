
def return_n_greatest_chars(input_string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(input_string, key=ord, reverse=True)
    # Take the top 44 characters from the sorted list
    greatest_chars = sorted_string[:44]
    return greatest_chars
