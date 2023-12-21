
def return_n_greatest_chars(input_string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(input_string, key=ord, reverse=True)
    # Return the top 88 characters of the sorted string
    return sorted_string[:88]
