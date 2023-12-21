 def filter_chars(my_string):
    # create a new empty string
    new_string = ""
    # iterate over each character in the input string
    for char in my_string:
        # if the current character is between indices 35 and 98, inclusive, and is greater than or equal to 'A' and smaller than or equal to 'b', then remove all occurrences of that character from the input string
        if (char.lower() >= "a" and char.lower() <= "b") and char.lower() in my_string[35:98]:
            # replace each occurrence of the current character with an empty string
            new_string = new_string + char.replace(char, "")
        # otherwise, just add the current character to the new string
        else:
            new_string = new_string + char
    # return the altered input string
    return new_string
