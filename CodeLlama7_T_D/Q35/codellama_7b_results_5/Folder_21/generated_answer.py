
def remove_repeat_chars(string):
    # Create a new string with the characters from the original string
    # that occur more than once between indices 462 and 995, exclusive
    new_string = ""
    for i in range(462, 995):
        if string[i] not in new_string:
            new_string += string[i]
    return new_string
