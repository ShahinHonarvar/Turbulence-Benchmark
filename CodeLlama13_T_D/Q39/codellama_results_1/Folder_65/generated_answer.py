
def return_n_greatest_chars(string):
    # Sort the string in descending order based on ASCII values
    sorted_chars = "".join(sorted(string, reverse=True))
    
    # Return a list of exactly 27 characters with the greatest ASCII values
    return sorted_chars[:27]
