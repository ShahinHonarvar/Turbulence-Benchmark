 def filter_chars(s):
    # create a new empty string
    result = ""

    # iterate through each character in the given string
    for char in s:
        # if the current character is between indices 2 and 3, both inclusive, and is greater than or equal to character '5' and smaller than or equal to character '_', then remove all occurrences of that character from the string
        if (char >= "5" and char <= "_") and s.index(char) in range(2,4):
            continue

        # else add the current character to the new string
        result += char

    # return the altered string
    return result
