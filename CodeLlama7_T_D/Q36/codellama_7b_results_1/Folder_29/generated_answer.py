 def filter_chars(s):
    # create a new string with the filtered characters
    new_string = ""

    # loop through each character in the given string
    for i in range(len(s)):

        # check if the current character is between indices 46 and 68 (both exclusive)
        if 46 < i < 68:

            # check if the current character is greater than 'H' and smaller than 's'
            if s[i] > 'H' and s[i] < 's':

                # skip over this character in the new string
                continue

        # add the current character to the new string
        new_string += s[i]

    # return the altered string
    return new_string
