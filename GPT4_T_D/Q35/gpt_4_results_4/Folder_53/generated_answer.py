
def remove_repeat_chars(input_string):
    sub_string = input_string[201:202]
    for char in set(sub_string):
        if sub_string.count(char) > 1:
            input_string = input_string.replace(char,'')
    return input_string
