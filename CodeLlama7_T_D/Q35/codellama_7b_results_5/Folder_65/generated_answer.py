
def remove_repeat_chars(string):
    # Initialize an empty list to store the characters that are not repeated
    non_repeated = []
    # Iterate through the string and check for each character if it is repeated or not
    for i in range(len(string)):
        # If the current character is not already in the non_repeated list, add it to the list
        if string[i] not in non_repeated:
            non_repeated.append(string[i])
    # Initialize an empty string to store the final result
    result = ""
    # Iterate through the non_repeated list and add each character to the result string
    for i in range(len(non_repeated)):
        result += non_repeated[i]
    # Return the final result string
    return result
