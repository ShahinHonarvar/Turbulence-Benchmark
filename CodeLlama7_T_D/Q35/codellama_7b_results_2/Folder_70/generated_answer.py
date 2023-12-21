
def remove_repeat_chars(string):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the given string
    for char in string:

        # If the current character does not occur more than once between indices 43 and 70, exclusive, then append it to the result string
        if string.count(char) <= 1:
            result += char

        # If the current character occurs more than once between indices 43 and 70, exclusive, then remove all occurrences of that character from the result string
        else:
            while result.find(char) != -1:
                index = result.find(char)
                result = result[:index] + result[index+1:]

    # Return the altered string
    return result
