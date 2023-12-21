
def remove_repeat_chars(input_string):
    char_dict = {}
    for x in range(37, 54):
        if x < len(input_string) and input_string[x] in char_dict:
            char_dict[input_string[x]] += 1
        elif x < len(input_string):
            char_dict[input_string[x]] = 1
    altered_string = ''.join([x for x in input_string if (x not in char_dict or char_dict[x] == 1)])

    return altered_string
