 def return_n_greatest_chars(input_string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(input_string, key=ord, reverse=True)
    # Take the top 12 characters from the sorted string
    greatest_chars = sorted_string[:12]
    # Return the list of greatest characters in ascending order
    return greatest_chars
