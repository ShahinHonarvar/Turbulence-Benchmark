
def filter_chars(input_string):
    unique_chars = set(input_string[2:9])
    for char in unique_chars:
        if "8" < char < "m":
            input_string = input_string.replace(char, "")
    return input_string
