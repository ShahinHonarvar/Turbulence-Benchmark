
def insert_after_character(string):
    # Create a new string with the same characters as the input string, but with 'i' inserted immediately after any occurrences of 'I'
    new_string = ""
    for i in range(len(string)):
        if string[i] == "I":
            new_string += "I" + "i"
        else:
            new_string += string[i]
    return new_string
