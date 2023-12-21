
def remove_repeat_chars(input_string):
    intermediate_string = list(input_string[50:74])
    for character in set(intermediate_string):
        if intermediate_string.count(character) > 1:
            input_string = input_string.replace(character, '')
    return input_string
