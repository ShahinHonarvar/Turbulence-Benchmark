
def remove_repeat_chars(s):
    # Create a set of unique characters in the string
    char_set = set(s)
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the string
    for char in s:
        # If the character is not in the set of unique characters, add it to the result string
        if char not in char_set:
            result += char

        # If the character is in the set of unique characters and its index is greater than 70 and less than 98 (exclusive), remove all occurrences of that character from the result string
        elif char_set.index(char) > 70 and char_set.index(char) < 98:
            while result.find(char) != -1:
                result = result[:result.find(char)] + result[result.find(char) + 1:]
    # Return the altered string
    return result
