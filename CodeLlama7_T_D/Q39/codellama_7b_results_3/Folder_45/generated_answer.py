
def return_n_greatest_chars(string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(string, key=ord, reverse=True)
    # Return the first 52 characters of the sorted string
    return ''.join(sorted_string[:52])
