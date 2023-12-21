
def remove_repeat_chars(input_string):
    sub_string = input_string[14:91]
    characters = set()
    output_string = ""
    for char in sub_string:
        if sub_string.count(char) > 1:
            characters.add(char)
    for char in input_string:
        if char not in characters:
            output_string += char
    return output_string
