
def filter_chars(input_string):
    candidate_chars = set(input_string[19:95])
    valid_chars = [char for char in candidate_chars if 'K' < char < 'a']
    for char in valid_chars:
        input_string = input_string.replace(char, '')
    return input_string
