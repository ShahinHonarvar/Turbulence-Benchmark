
def filter_chars(input_string):
    altered_chars = [character for idx, character in enumerate(input_string) if not(25 <= idx <= 97 and 'm' <= character <= 'w')]
    result = "".join(altered_chars)
    return result
