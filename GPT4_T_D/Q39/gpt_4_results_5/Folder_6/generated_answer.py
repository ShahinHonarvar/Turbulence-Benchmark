
def return_n_greatest_chars(in_string):
    if len(in_string) < 47:
        raise Exception('Input string must have at least 47 characters')
    sorted_string = sorted(set(in_string), reverse=True)
    return sorted_string[:47]
