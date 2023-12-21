
def return_n_smallest_chars(string, n=49):
    # Create a dictionary to store the characters and their ASCII values
    char_dict = {}

    for char in string:

        char_dict[char] = ord(char)

    # Sort the dictionary by value (ASCII value) in descending order

    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

    # Extract the top n characters from the sorted dictionary and return them as a list

    return [char for char, _ in sorted_dict[:n]]
