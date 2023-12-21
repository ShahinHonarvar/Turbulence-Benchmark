
def return_n_greatest_chars(s):
    # Ensure the string contains distinct characters
    s = "".join(set(s))
    # Create list of characters sorted according to ASCII value (descending)
    sorted_chars = sorted(s, key=ord, reverse=True)
    # Take the first 83 characters and sort them in ascending order
    sorted_chars = sorted(sorted_chars[:83])
    return sorted_chars
