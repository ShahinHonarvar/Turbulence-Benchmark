
def insert_before_character(string, character):
    # Find the index of the first occurrence of the character
    index = string.find(character)

    # If the character is found in the string, insert it before the character
    if index != -1:
        return string[:index] + character + string[index:]

    # If the character is not found in the string, return the original string
    else:
        return string
