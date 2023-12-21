 def return_n_greatest_chars(string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(string, key=ord, reverse=True)
    # Take the top 35 characters from the sorted list
    greatest_chars = sorted_string[:35]
    # Return the sorted list of 35 greatest characters in ascending order
    return greatest_chars
