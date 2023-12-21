
def remove_repeat_chars(input_string):
    str_range = input_string[45:91]
    removed_chars = [char for char in str_range if str_range.count(char) == 1]
    rest_string = input_string[:45] + "".join(removed_chars) + input_string[91:]
    return rest_string
