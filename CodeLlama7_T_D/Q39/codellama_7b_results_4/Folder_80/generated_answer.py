
def return_n_greatest_chars(string):
    # Sort the string in descending order based on ASCII value
    sorted_list = sorted(string, key=ord, reverse=True)
    # Return the top 35 characters from the sorted list
    return sorted_list[:35]
