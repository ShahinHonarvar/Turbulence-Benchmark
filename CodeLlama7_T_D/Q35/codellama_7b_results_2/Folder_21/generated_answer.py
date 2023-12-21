
def remove_repeat_chars(s):
    # Create a new string with all characters from the original string
    # that occur more than once between indices 462 and 995 removed
    new_string = ""

    # Iterate over all characters in the original string

    for char in s:

        # Check if the current character occurs more than once between indices 462 and 995

        if s.count(char) > 1 and (s.index(char)) >= 462 and (s.index(char)) <= 995:

            # If it does, remove all occurrences of that character from the original string

            new_string += char

    return new_string
