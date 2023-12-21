
def return_n_smallest_chars(string, n=56):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create an empty list to store the smallest ASCII values
    smallest_ascii_values = []

    for char in char_list:
        # Append the ASCII value of each character to the list
        smallest_ascii_values.append(ord(char))

    # Sort the list in descending order using the built-in sort() method and the key function
    smallest_ascii_values.sort(key=lambda x: -x)

    # Return the first n elements of the sorted list
    return smallest_ascii_values[:n]
