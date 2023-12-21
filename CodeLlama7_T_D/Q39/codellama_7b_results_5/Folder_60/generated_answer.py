
def return_n_greatest_chars(s, n):
    # Sort the string in descending order based on ASCII value
    sorted_str = sorted(s, key=ord, reverse=True)
    # Return the top 'n' characters from the sorted list
    return sorted_str[:n]
