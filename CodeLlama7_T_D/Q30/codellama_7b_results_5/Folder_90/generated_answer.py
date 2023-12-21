 def insert_before_character(string):
    # Initialize an empty string to store the result
    result = ""
    # Iterate over each character in the input string
    for char in string:
        # If the current character is 'U', insert the character 'F' before it and continue with the next character
        if char == "U":
            result += "F" + char
        else:
            result += char

    return result
