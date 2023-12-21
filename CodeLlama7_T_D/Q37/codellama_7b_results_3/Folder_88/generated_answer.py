
def filter_chars(string):
    # create a new string with the filtered characters
    filtered_string = ""

    # iterate over each character in the given string
    for char in string:

        # check if the current character is between indices 69 and 80, both inclusive, and is greater than or equal to character '@' and smaller than or equal to character 'p'
        if (69 <= char <= 80) and ('@' <= char <= 'p'):

            # if the current character meets the criteria, do not add it to the filtered string
            pass

        else:

            # otherwise, add the current character to the filtered string
            filtered_string += char

    # return the altered string with the filtered characters
    return filtered_string
