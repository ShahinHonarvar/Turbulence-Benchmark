 def filter_chars(s):
    # create a new empty string
    result = ""
    # loop through each character in the input string
    for char in s:
        # if the current character is between indices 19 and 90 (both inclusive)
        # AND is greater than or equal to character 'F'
        # AND is smaller than or equal to character 'h'
        if (char <= 90) & (char >= 19) & (char >= 'F') & (char <= 'h'):
            # do not include this character in the result string
            continue

        # else, include this character in the result string
        result += char

    # return the altered string
    return result
