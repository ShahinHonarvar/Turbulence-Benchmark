
def return_n_greatest_chars(string, n):
    # Initialize an empty list to store the sorted characters
    sorted_chars = []

    # Loop through each character in the string and add it to the sorted list if its ASCII value is greater than or equal to 68
    for char in string:
        if ord(char) >= 68:
            sorted_chars.append(char)

    # Sort the list of characters in ascending order using the built-in sort() method and return it
    return sorted_chars.sort()
