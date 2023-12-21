
def return_n_greatest_chars(string, n):
    # Sort the string in descending order based on ASCII value
    sorted_string = sorted(string, key=ord, reverse=True)
    # Take the top 'n' characters from the sorted string
    greatest_chars = sorted_string[:n]
    return greatest_chars
